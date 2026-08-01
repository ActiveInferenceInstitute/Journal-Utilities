/**
 * Active Inference Institute — SPA Application
 *
 * Client-side router, video library, search, audio player, and LLM chat
 * with streaming responses and RAG context display.
 */

// ---------------------------------------------------------------------------
// State
// ---------------------------------------------------------------------------

const state = {
    videos: [],
    totalVideos: 0,
    currentPage: 0,
    pageSize: 48,
    searchQuery: '',
    activeCategory: null,
    categories: {},
    stats: {},
    currentVideoId: null,
    chatSessionId: 'session_' + Date.now(),
    chatAvailable: false,
    chatStreaming: false,
};

// ---------------------------------------------------------------------------
// API helpers
// ---------------------------------------------------------------------------

async function api(path, options = {}) {
    const resp = await fetch(`/api${path}`, {
        headers: { 'Content-Type': 'application/json' },
        ...options,
    });
    if (!resp.ok) throw new Error(`API ${path}: ${resp.status}`);
    return resp.json();
}

function debounce(fn, ms) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), ms);
    };
}

function formatDuration(seconds) {
    if (!seconds) return '';
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = Math.floor(seconds % 60);
    if (h > 0) return `${h}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    return `${m}:${s.toString().padStart(2, '0')}`;
}

function formatDate(dateStr) {
    if (!dateStr) return '';
    // Handle YYYYMMDD format
    if (dateStr.length === 8 && !dateStr.includes('-')) {
        return `${dateStr.slice(0, 4)}-${dateStr.slice(4, 6)}-${dateStr.slice(6, 8)}`;
    }
    // Already formatted (YYYY-MM-DD) or other format
    return dateStr;
}

function formatBytes(bytes) {
    if (!bytes) return '';
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
    if (bytes < 1073741824) return (bytes / 1048576).toFixed(1) + ' MB';
    return (bytes / 1073741824).toFixed(2) + ' GB';
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

/** Video IDs are interpolated into inline JS/href/attribute contexts; only
 *  canonical YouTube ids ([A-Za-z0-9_-]{11}) are safe to accept there. */
function safeVideoId(id) {
    return /^[A-Za-z0-9_-]{11}$/.test(String(id || '')) ? String(id) : '';
}

/** Shorten hierarchical category names for display. */
function shortCategoryName(name) {
    if (!name) return '';
    // "TextbookGroup/ParrPezzuloFriston2022/Cohort_1" → "Cohort 1"
    // "Courses/PhysicsAsInformationProcessing" → "Physics As Information Processing"
    const parts = name.split('/');
    let display = parts[parts.length - 1];  // take last segment
    // Convert underscores and camelCase to spaces
    display = display.replace(/_/g, ' ');
    display = display.replace(/([a-z])([A-Z])/g, '$1 $2');
    return display;
}

// Simple markdown-to-HTML for chat. Escape FIRST so any raw HTML the model
// emits (or that arrives via transcript context) can never execute; the
// markdown transforms then only wrap already-escaped content in tags.
function renderMarkdown(text) {
    return escapeHtml(text == null ? '' : String(text))
        .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
        .replace(/`([^`]+)`/g, '<code>$1</code>')
        .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
        .replace(/\*([^*]+)\*/g, '<em>$1</em>')
        .replace(/\$([^$]+)\$/g, '<em class="math">$1</em>')
        .replace(/^### (.+)$/gm, '<h4>$1</h4>')
        .replace(/^## (.+)$/gm, '<h3>$1</h3>')
        .replace(/^# (.+)$/gm, '<h2>$1</h2>')
        .replace(/^[•\-] (.+)$/gm, '<li>$1</li>')
        .replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>')
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>');
}

// ---------------------------------------------------------------------------
// Tab navigation
// ---------------------------------------------------------------------------

function switchTab(tabName) {
    // Update nav tabs
    document.querySelectorAll('.nav-tab').forEach(btn => {
        const isActive = btn.dataset.tab === tabName;
        btn.classList.toggle('nav-tab--active', isActive);
        btn.setAttribute('aria-selected', isActive);
    });

    // Update panels
    document.querySelectorAll('.tab-panel').forEach(panel => {
        panel.classList.remove('tab-panel--active');
    });

    const panel = document.getElementById(`panel-${tabName}`);
    if (panel) panel.classList.add('tab-panel--active');

    // Load data on first visit
    if (tabName === 'knowledge' && !document.getElementById('categoryGrid').children.length) {
        loadKnowledge();
    }
    if (tabName === 'chat' && state.chatAvailable === false) {
        checkChatStatus();
    }
}

function showVideoDetail(videoId) {
    state.currentVideoId = videoId;
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('tab-panel--active'));
    document.getElementById('panel-detail').classList.add('tab-panel--active');
    loadVideoDetail(videoId);
}

function backToLibrary() {
    state.currentVideoId = null;
    document.getElementById('panel-detail').classList.remove('tab-panel--active');
    document.getElementById('panel-library').classList.add('tab-panel--active');
}

// ---------------------------------------------------------------------------
// Library
// ---------------------------------------------------------------------------

async function loadStats() {
    try {
        const stats = await api('/stats');
        state.stats = stats;
        const bar = document.getElementById('statsBar');
        bar.innerHTML = `
            <div class="stat-card">
                <div class="stat-card__value">${stats.total_videos}</div>
                <div class="stat-card__label">Total Videos</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.with_transcripts}</div>
                <div class="stat-card__label">Transcripts</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.with_audio}</div>
                <div class="stat-card__label">Audio Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.total_transcript_mb} MB</div>
                <div class="stat-card__label">Transcript Data</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.total_audio_gb} GB</div>
                <div class="stat-card__label">Audio Data</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.category_count}</div>
                <div class="stat-card__label">Categories</div>
            </div>
        `;
    } catch (e) {
        console.error('Failed to load stats:', e);
    }
}

async function loadCategories() {
    try {
        const data = await api('/categories');
        state.categories = data.categories;
        const bar = document.getElementById('filterBar');
        bar.innerHTML = '<span class="filter-bar__label">Filter:</span>';

        // All chip
        const allBtn = document.createElement('button');
        allBtn.className = 'filter-chip filter-chip--active';
        allBtn.textContent = 'All';
        allBtn.onclick = () => filterByCategory(null);
        bar.appendChild(allBtn);

        // Category chips sorted by count
        const sorted = Object.entries(data.categories).sort((a, b) => b[1] - a[1]);
        for (const [cat, count] of sorted) {
            const btn = document.createElement('button');
            btn.className = 'filter-chip';
            btn.dataset.category = cat;
            btn.title = cat;  // Full name on hover
            btn.innerHTML = `${escapeHtml(shortCategoryName(cat))}<span class="filter-chip__count">${count}</span>`;
            btn.onclick = () => filterByCategory(cat);
            bar.appendChild(btn);
        }
    } catch (e) {
        console.error('Failed to load categories:', e);
    }
}

function filterByCategory(category) {
    state.activeCategory = category;
    state.currentPage = 0;

    // Update chip styles
    document.querySelectorAll('.filter-chip').forEach(chip => {
        const isActive = category === null
            ? !chip.dataset.category
            : chip.dataset.category === category;
        chip.classList.toggle('filter-chip--active', isActive);
    });

    loadVideos();
}

async function loadVideos() {
    const grid = document.getElementById('videoGrid');
    grid.innerHTML = '<div class="loading"><div class="spinner"></div></div>';

    try {
        const params = new URLSearchParams({
            offset: state.currentPage * state.pageSize,
            limit: state.pageSize,
        });

        if (state.searchQuery) {
            params.set('q', state.searchQuery);
        }
        if (state.activeCategory) {
            params.set('category', state.activeCategory);
        }

        const data = await api(`/videos?${params}`);
        state.videos = data.videos;
        state.totalVideos = data.total;

        renderVideoGrid(data.videos, !!state.searchQuery);
        renderPagination();
    } catch (e) {
        grid.innerHTML = `
            <div class="empty-state">
                <div class="empty-state__icon">⚠️</div>
                <div class="empty-state__title">Failed to load videos</div>
                <div class="empty-state__desc">${escapeHtml(e.message)}</div>
            </div>
        `;
    }
}

function renderVideoGrid(videos, isSearch) {
    const grid = document.getElementById('videoGrid');

    if (!videos.length) {
        grid.innerHTML = `
            <div class="empty-state">
                <div class="empty-state__icon">${isSearch ? '🔍' : '📭'}</div>
                <div class="empty-state__title">${isSearch ? 'No results found' : 'No videos'}</div>
                <div class="empty-state__desc">
                    ${isSearch ? 'Try different keywords or clear filters' : 'Video data is loading...'}
                </div>
            </div>
        `;
        return;
    }

    grid.innerHTML = videos.map(v => `
        <article class="video-card" onclick="showVideoDetail('${safeVideoId(v.id)}')" tabindex="0"
                 role="button" aria-label="View ${escapeHtml(v.title || v.id)}"
                 data-video-id="${safeVideoId(v.id)}">
            <div class="video-card__thumb">
                <img src="${v.thumbnail_url}" alt="" loading="lazy"
                     onerror="this.style.display='none'">
                ${v.duration ? `<span class="video-card__duration">${formatDuration(v.duration)}</span>` : ''}
                <div class="video-card__badges">
                    ${v.has_transcript ? '<span class="badge badge--transcript">📝 Transcript</span>' : ''}
                    ${v.has_audio ? '<span class="badge badge--audio">🎧 Audio</span>' : ''}
                </div>
            </div>
            <div class="video-card__body">
                <div class="video-card__title">${escapeHtml(v.title || v.id)}</div>
                <div class="video-card__meta">
                    ${v.upload_date ? `<span>${formatDate(v.upload_date)}</span>` : ''}
                    ${v.category ? `<span class="video-card__category">${escapeHtml(v.category)}</span>` : ''}
                </div>
                ${v.search_snippet ? `<div class="video-card__snippet">${escapeHtml(v.search_snippet)}</div>` : ''}
            </div>
        </article>
    `).join('');
}

function renderPagination() {
    const container = document.getElementById('pagination');
    const totalPages = Math.ceil(state.totalVideos / state.pageSize);

    if (totalPages <= 1) {
        container.innerHTML = '';
        return;
    }

    let html = '';

    // Previous
    html += `<button class="page-btn" onclick="goToPage(${state.currentPage - 1})"
             ${state.currentPage === 0 ? 'disabled' : ''}>← Prev</button>`;

    // Page numbers
    const start = Math.max(0, state.currentPage - 2);
    const end = Math.min(totalPages, start + 5);

    for (let i = start; i < end; i++) {
        html += `<button class="page-btn ${i === state.currentPage ? 'page-btn--active' : ''}"
                 onclick="goToPage(${i})">${i + 1}</button>`;
    }

    // Next
    html += `<button class="page-btn" onclick="goToPage(${state.currentPage + 1})"
             ${state.currentPage >= totalPages - 1 ? 'disabled' : ''}>Next →</button>`;

    // Info
    html += `<span class="pagination__info">${state.totalVideos} videos</span>`;

    container.innerHTML = html;
}

function goToPage(page) {
    const totalPages = Math.ceil(state.totalVideos / state.pageSize);
    if (page < 0 || page >= totalPages) return;
    state.currentPage = page;
    loadVideos();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Search
const doSearch = debounce(() => {
    state.currentPage = 0;
    loadVideos();
}, 300);

// ---------------------------------------------------------------------------
// Video Detail
// ---------------------------------------------------------------------------

async function loadVideoDetail(videoId) {
    const container = document.getElementById('videoDetailContent');
    container.innerHTML = '<div class="loading"><div class="spinner"></div></div>';

    try {
        const video = await api(`/videos/${videoId}`);
        let transcriptHtml = '';
        let audioHtml = '';

        // Load transcript
        if (video.has_transcript) {
            try {
                const tData = await api(`/transcripts/${videoId}`);
                transcriptHtml = `
                    <div class="transcript-panel">
                        <div class="transcript-panel__header">
                            <span class="transcript-panel__title">📝 Full Transcript</span>
                            <span class="transcript-panel__size">${formatBytes(video.transcript_size)}</span>
                        </div>
                        <div class="transcript-panel__body">${escapeHtml(tData.text)}</div>
                    </div>
                `;
            } catch (e) {
                transcriptHtml = '<p class="text-muted">Failed to load transcript.</p>';
            }
        }

        // Audio player
        if (video.has_audio) {
            audioHtml = `
                <div class="audio-player">
                    <div class="audio-player__header">🎧 Audio Player</div>
                    <audio controls preload="none" id="audioPlayer">
                        <source src="/api/audio/${videoId}" type="audio/mpeg">
                        Your browser does not support audio playback.
                    </audio>
                    ${video.audio_size ? `<div class="audio-player__filesize">${formatBytes(video.audio_size)}</div>` : ''}
                </div>
            `;
        }

        container.innerHTML = `
            <div class="video-detail">
                <div class="video-detail__main">
                    <!-- YouTube embed -->
                    <div class="video-player">
                        <iframe src="https://www.youtube.com/embed/${safeVideoId(videoId)}"
                                title="${escapeHtml(video.title || videoId)}"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowfullscreen></iframe>
                    </div>

                    <!-- Title & meta -->
                    <h1 class="video-detail__title">${escapeHtml(video.title || videoId)}</h1>
                    <div class="video-detail__meta-row">
                        ${video.upload_date ? `<span class="video-detail__meta-item">📅 ${formatDate(video.upload_date)}</span>` : ''}
                        ${video.duration ? `<span class="video-detail__meta-item">⏱ ${formatDuration(video.duration)}</span>` : ''}
                        ${video.category ? `<span class="video-detail__meta-item video-card__category">${escapeHtml(video.category)}</span>` : ''}
                        ${video.series ? `<span class="video-detail__meta-item">📺 ${escapeHtml(video.series)}</span>` : ''}
                    </div>

                    <!-- Audio -->
                    ${audioHtml}

                    <!-- Transcript -->
                    ${transcriptHtml}
                </div>

                <div class="video-detail__sidebar">
                    <!-- Metadata card -->
                    <div class="meta-card">
                        <div class="meta-card__title">Video Information</div>
                        <div class="meta-card__row">
                            <span class="meta-card__key">Video ID</span>
                            <span class="meta-card__value meta-card__value--mono">${videoId}</span>
                        </div>
                        ${video.category ? `<div class="meta-card__row"><span class="meta-card__key">Category</span><span class="meta-card__value">${escapeHtml(video.category)}</span></div>` : ''}
                        ${video.series ? `<div class="meta-card__row"><span class="meta-card__key">Series</span><span class="meta-card__value">${escapeHtml(video.series)}</span></div>` : ''}
                        ${video.episode ? `<div class="meta-card__row"><span class="meta-card__key">Episode</span><span class="meta-card__value">${escapeHtml(video.episode)}</span></div>` : ''}
                        <div class="meta-card__row">
                            <span class="meta-card__key">Transcript</span>
                            <span class="meta-card__value">${video.has_transcript ? '<span style="color:var(--accent-primary)">● Available</span>' : '<span class="text-muted">✕ None</span>'}</span>
                        </div>
                        <div class="meta-card__row">
                            <span class="meta-card__key">Audio</span>
                            <span class="meta-card__value">${video.has_audio ? '<span style="color:var(--accent-primary)">● Available</span>' : '<span class="text-muted">✕ None</span>'}</span>
                        </div>
                         ${video.has_transcript ? `<div class="meta-card__row"><span class="meta-card__key">Transcript size</span><span class="meta-card__value">${formatBytes(video.transcript_size)}</span></div>` : ''}
                         ${video.audio_size ? `<div class="meta-card__row"><span class="meta-card__key">Audio size</span><span class="meta-card__value">${formatBytes(video.audio_size)}</span></div>` : ''}
                    </div>

                    <!-- Links card -->
                    <div class="meta-card">
                        <div class="meta-card__title">Links</div>
                        <div class="meta-card__row">
                            <a href="${video.youtube_url}" target="_blank" rel="noopener"
                               style="color:var(--accent-primary);">
                                ▶ Watch on YouTube
                            </a>
                        </div>
                        ${video.has_transcript ? `<div class="meta-card__row">
                            <a href="#" onclick="askAboutVideo('${safeVideoId(videoId)}'); return false;"
                               style="color:var(--accent-warm);">
                                💬 Ask AI about this video
                            </a>
                        </div>` : ''}
                    </div>
                </div>
            </div>
        `;
    } catch (e) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state__icon">⚠️</div>
                <div class="empty-state__title">Video not found</div>
                <div class="empty-state__desc">${escapeHtml(e.message)}</div>
            </div>
        `;
    }
}

function askAboutVideo(videoId) {
    const video = state.videos.find(v => v.id === videoId);
    const title = video ? video.title : videoId;
    switchTab('chat');
    const input = document.getElementById('chatInput');
    input.value = `Tell me about the video "${title}" and summarize its key insights.`;
    input.focus();
}

// ---------------------------------------------------------------------------
// Knowledge / Stats
// ---------------------------------------------------------------------------

async function loadKnowledge() {
    try {
        const stats = state.stats.total_videos ? state.stats : await api('/stats');
        state.stats = stats;

        // Stats bar
        const knowledgeStats = document.getElementById('knowledgeStats');
        knowledgeStats.innerHTML = `
            <div class="stat-card">
                <div class="stat-card__value">${stats.total_videos}</div>
                <div class="stat-card__label">Videos Indexed</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.with_transcripts}</div>
                <div class="stat-card__label">Searchable Transcripts</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.total_transcript_mb} MB</div>
                <div class="stat-card__label">Research Text</div>
            </div>
            <div class="stat-card">
                <div class="stat-card__value">${stats.category_count}</div>
                <div class="stat-card__label">Content Series</div>
            </div>
        `;

        // Category grid
        const catGrid = document.getElementById('categoryGrid');
        const cats = stats.categories || {};
        const maxCount = Math.max(...Object.values(cats), 1);
        const sorted = Object.entries(cats).sort((a, b) => b[1] - a[1]);

        catGrid.innerHTML = sorted.map(([cat, count]) => `
            <div class="category-card" onclick="filterByCategory('${escapeHtml(cat)}'); switchTab('library');" title="${escapeHtml(cat)}">
                <div class="category-card__name">${escapeHtml(shortCategoryName(cat))}</div>
                <div class="category-card__count">${count}</div>
                <div class="category-card__bar">
                    <div class="category-card__fill" style="width: ${(count / maxCount * 100).toFixed(1)}%"></div>
                </div>
            </div>
        `).join('');

    } catch (e) {
        console.error('Failed to load knowledge:', e);
    }
}

// ---------------------------------------------------------------------------
// Chat
// ---------------------------------------------------------------------------

async function checkChatStatus() {
    try {
        const status = await api('/chat/status');
        state.chatAvailable = status.available;
        const dot = document.getElementById('chatDot');
        const text = document.getElementById('chatStatusText');
        const sendBtn = document.getElementById('chatSend');

        if (status.available) {
            dot.classList.add('chat-header__dot--online');
            text.textContent = `Connected — ${status.current_model}`;
            sendBtn.disabled = false;
        } else {
            dot.classList.remove('chat-header__dot--online');
            text.textContent = status.message || 'Ollama not available';
            sendBtn.disabled = true;
        }
    } catch (e) {
        document.getElementById('chatStatusText').textContent = 'API unavailable';
    }
}

async function sendChatMessage() {
    const input = document.getElementById('chatInput');
    const message = input.value.trim();
    if (!message || state.chatStreaming) return;

    const useRag = document.getElementById('ragToggle').checked;

    // Hide welcome
    const welcome = document.getElementById('chatWelcome');
    if (welcome) welcome.style.display = 'none';

    // Add user message
    appendChatMessage('user', message);
    input.value = '';
    input.style.height = 'auto';
    state.chatStreaming = true;
    document.getElementById('chatSend').disabled = true;

    // Show typing indicator
    const messagesEl = document.getElementById('chatMessages');
    const typingEl = document.createElement('div');
    typingEl.className = 'typing-indicator';
    typingEl.id = 'typingIndicator';
    typingEl.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
    messagesEl.appendChild(typingEl);
    messagesEl.scrollTop = messagesEl.scrollHeight;

    try {
        const resp = await fetch('/api/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                session_id: state.chatSessionId,
                message,
                use_rag: useRag,
            }),
        });

        // Remove typing indicator
        typingEl.remove();

        if (!resp.ok) throw new Error(`Chat error: ${resp.status}`);

        // Create assistant message element
        const msgEl = document.createElement('div');
        msgEl.className = 'chat-message chat-message--assistant';
        messagesEl.appendChild(msgEl);

        let fullText = '';
        let contextIds = [];

        const reader = resp.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
                if (!line.startsWith('data: ')) continue;
                try {
                    const data = JSON.parse(line.slice(6));

                    if (data.type === 'context' && data.video_ids?.length) {
                        contextIds = data.video_ids;
                        const ctxHtml = contextIds.map(id =>
                            `<span class="chat-context-tag" onclick="showVideoDetail('${safeVideoId(id)}')"
                                   title="View source">📄 ${escapeHtml(safeVideoId(id))}</span>`
                        ).join('');
                        msgEl.innerHTML = `<div class="chat-message__context">${ctxHtml}</div>`;
                    }

                    if (data.type === 'token') {
                        fullText += data.content;
                        const ctxEl = msgEl.querySelector('.chat-message__context');
                        const rendered = renderMarkdown(fullText);
                        msgEl.innerHTML = (ctxEl ? ctxEl.outerHTML : '') + rendered;
                        messagesEl.scrollTop = messagesEl.scrollHeight;
                    }

                    if (data.type === 'error') {
                        msgEl.innerHTML += `<p style="color:var(--accent-danger);">Error: ${escapeHtml(data.message)}</p>`;
                    }
                } catch (parseErr) {
                    // skip malformed SSE
                }
            }
        }
    } catch (e) {
        if (typingEl.parentNode) typingEl.remove();
        appendChatMessage('assistant', `⚠️ Error: ${e.message}`);
    }

    state.chatStreaming = false;
    document.getElementById('chatSend').disabled = !state.chatAvailable;
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function appendChatMessage(role, content) {
    const messagesEl = document.getElementById('chatMessages');
    const msgEl = document.createElement('div');
    msgEl.className = `chat-message chat-message--${role}`;
    msgEl.innerHTML = role === 'user' ? escapeHtml(content) : renderMarkdown(content);
    messagesEl.appendChild(msgEl);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

async function clearChat() {
    try {
        await fetch('/api/chat/clear', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id: state.chatSessionId }),
        });
    } catch (e) { /* ignore */ }

    state.chatSessionId = 'session_' + Date.now();
    const messagesEl = document.getElementById('chatMessages');
    messagesEl.innerHTML = `
        <div class="chat-welcome" id="chatWelcome">
            <div class="chat-welcome__icon">🧠</div>
            <div class="chat-welcome__title">Active Inference Research Assistant</div>
            <div class="chat-welcome__desc">
                Ask questions about Active Inference, the Free Energy Principle,
                or any topic covered in the Institute's video library.
                Responses are grounded in real transcript data.
            </div>
            <div class="chat-welcome__suggestions" id="chatSuggestions">
                <button class="chat-suggestion" data-q="What is the Free Energy Principle?">What is the Free Energy Principle?</button>
                <button class="chat-suggestion" data-q="Explain Markov blankets in active inference">Explain Markov blankets</button>
                <button class="chat-suggestion" data-q="What are the latest developments in active inference?">Latest developments</button>
                <button class="chat-suggestion" data-q="How does predictive coding relate to active inference?">Predictive coding</button>
            </div>
        </div>
    `;

    // Re-bind suggestion buttons
    bindSuggestions();
}

function bindSuggestions() {
    document.querySelectorAll('.chat-suggestion').forEach(btn => {
        btn.onclick = () => {
            document.getElementById('chatInput').value = btn.dataset.q;
            sendChatMessage();
        };
    });
}

// ---------------------------------------------------------------------------
// Initialization
// ---------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', () => {
    // Tab navigation
    document.querySelectorAll('.nav-tab').forEach(btn => {
        btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });

    // Back button
    document.getElementById('backToLibrary').addEventListener('click', (e) => {
        e.preventDefault();
        backToLibrary();
    });

    // Search
    const searchInput = document.getElementById('searchInput');
    const searchClear = document.getElementById('searchClear');

    searchInput.addEventListener('input', () => {
        state.searchQuery = searchInput.value.trim();
        searchClear.classList.toggle('search-bar__clear--visible', !!state.searchQuery);
        doSearch();
    });

    searchClear.addEventListener('click', () => {
        searchInput.value = '';
        state.searchQuery = '';
        searchClear.classList.remove('search-bar__clear--visible');
        loadVideos();
    });

    // Chat input
    const chatInput = document.getElementById('chatInput');
    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendChatMessage();
        }
    });

    // Auto-resize chat input
    chatInput.addEventListener('input', () => {
        chatInput.style.height = 'auto';
        chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + 'px';
    });

    document.getElementById('chatSend').addEventListener('click', sendChatMessage);
    document.getElementById('chatClear').addEventListener('click', clearChat);

    // Suggestion buttons
    bindSuggestions();

    // Video card keyboard support
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && e.target.classList.contains('video-card')) {
            const id = e.target.dataset.videoId;
            if (id) showVideoDetail(id);
        }
    });

    // Load initial data
    loadStats();
    loadCategories();
    loadVideos();
});
