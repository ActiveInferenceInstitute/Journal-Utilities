/**
 * Active Inference Journal — GitHub Pages Interactive App
 *
 * Client-side Single Page Application handling:
 * - Routing & views (#/ for library, #/item/:id for video/transcript viewer)
 * - YouTube IFrame API integration with interactive timestamp seeking
 * - Live transcript synchronization & cue highlighting
 * - Real-time multi-language subtitle translation switching
 * - In-browser fuzzy search and series filtering
 */

const state = {
    manifest: null,
    items: [],
    filteredItems: [],
    currentSeries: 'All',
    searchQuery: '',
    currentItem: null,
    currentPartIndex: 0,
    currentLanguage: 'original',
    ytPlayer: null,
    syncInterval: null,
};

const LANGUAGE_LABELS = {
    'original': 'Original Transcript (English)',
    'en': 'English',
    'es': 'Spanish (Español)',
    'fr': 'French (Français)',
    'de': 'German (Deutsch)',
    'pt': 'Portuguese (Português)',
    'it': 'Italian (Italiano)',
    'nl': 'Dutch (Nederlands)',
    'ru': 'Russian (Русский)',
    'ja': 'Japanese (日本語)',
    'ko': 'Korean (한국어)',
    'zh-Hans': 'Chinese Simplified (简体中文)',
    'zh-Hant': 'Chinese Traditional (繁體中文)',
};

function formatTime(seconds) {
    if (isNaN(seconds) || seconds === null) return '00:00';
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = Math.floor(seconds % 60);
    if (h > 0) {
        return `${h}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    }
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str || '';
    return div.innerHTML;
}

let isYouTubeApiReady = false;
window.onYouTubeIframeAPIReady = function () {
    isYouTubeApiReady = true;
};

function createOrUpdatePlayer(videoId, initialTime = 0) {
    if (state.ytPlayer && typeof state.ytPlayer.destroy === 'function') {
        try {
            state.ytPlayer.destroy();
        } catch (e) {
            console.warn('Error destroying player', e);
        }
        state.ytPlayer = null;
    }

    const container = document.getElementById('ytPlayerContainer');
    if (!container) return;

    container.innerHTML = '<div id="ytIframe"></div>';

    if (window.YT && window.YT.Player) {
        state.ytPlayer = new window.YT.Player('ytIframe', {
            videoId: videoId,
            playerVars: {
                autoplay: 0,
                modestbranding: 1,
                rel: 0,
                start: Math.floor(initialTime),
            },
            events: {
                onStateChange: onPlayerStateChange,
            },
        });
    } else {
        container.innerHTML = `
            <iframe src="https://www.youtube.com/embed/${encodeURIComponent(videoId)}?enablejsapi=1"
                    title="Video player"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
        `;
    }
}

function onPlayerStateChange(event) {
    if (event.data === window.YT.PlayerState.PLAYING) {
        startTranscriptSync();
    } else {
        stopTranscriptSync();
    }
}

function startTranscriptSync() {
    stopTranscriptSync();
    state.syncInterval = setInterval(() => {
        if (!state.ytPlayer || typeof state.ytPlayer.getCurrentTime !== 'function') return;
        const currentTime = state.ytPlayer.getCurrentTime();
        highlightActiveCue(currentTime);
    }, 400);
}

function stopTranscriptSync() {
    if (state.syncInterval) {
        clearInterval(state.syncInterval);
        state.syncInterval = null;
    }
}

function seekToTime(seconds) {
    if (state.ytPlayer && typeof state.ytPlayer.seekTo === 'function') {
        state.ytPlayer.seekTo(seconds, true);
        if (typeof state.ytPlayer.playVideo === 'function') {
            state.ytPlayer.playVideo();
        }
    }
}

async function init() {
    try {
        const resp = await fetch('manifest.json');
        if (!resp.ok) throw new Error('Failed to load manifest.json');
        state.manifest = await resp.json();
        state.items = state.manifest.items || [];
        state.filteredItems = [...state.items];

        window.addEventListener('hashchange', handleRoute);
        handleRoute();
    } catch (e) {
        const app = document.getElementById('app');
        app.innerHTML = `
            <div class="loading-state">
                <h2>⚠️ Error Loading Library</h2>
                <p>${escapeHtml(e.message)}</p>
            </div>
        `;
    }
}

function handleRoute() {
    stopTranscriptSync();
    const hash = window.location.hash || '#/';

    if (hash.startsWith('#/item/')) {
        const itemKey = decodeURIComponent(hash.replace('#/item/', ''));
        renderItemView(itemKey);
    } else {
        renderLibraryView();
    }
}

function renderLibraryView() {
    const app = document.getElementById('app');

    const seriesSet = new Set(['All']);
    state.items.forEach(it => {
        if (it.series) seriesSet.add(it.series);
    });
    const seriesList = Array.from(seriesSet);

    filterItems();

    app.innerHTML = `
        <div class="stats-strip">
            <div class="stat-chip">Total Items: <strong>${state.items.length}</strong></div>
            <div class="stat-chip">With Transcripts: <strong>${state.items.filter(i => i.has_transcript).length}</strong></div>
            <div class="stat-chip">Translated Items: <strong>${state.items.filter(i => i.languages && i.languages.length > 0).length}</strong></div>
            <div class="stat-chip">Series Categories: <strong>${seriesList.length - 1}</strong></div>
        </div>

        <div class="filter-section">
            <div class="search-wrapper">
                <input type="search" class="search-input" id="searchInput"
                       placeholder="Search videos, topics, series, or transcripts..."
                       value="${escapeHtml(state.searchQuery)}">
            </div>
            <div class="series-pills" id="seriesPills">
                ${seriesList.map(s => `
                    <button class="pill ${s === state.currentSeries ? 'active' : ''}" data-series="${escapeHtml(s)}">
                        ${escapeHtml(s)}
                    </button>
                `).join('')}
            </div>
        </div>

        <div class="video-grid" id="videoGrid">
            ${state.filteredItems.length === 0 ? `
                <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; color: var(--text-muted);">
                    No videos found matching your criteria.
                </div>
            ` : state.filteredItems.map(renderVideoCard).join('')}
        </div>
    `;

    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        filterItems();
        updateVideoGrid();
    });

    const pills = document.querySelectorAll('.pill');
    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            state.currentSeries = pill.getAttribute('data-series');
            document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            filterItems();
            updateVideoGrid();
        });
    });
}

function filterItems() {
    const q = state.searchQuery.toLowerCase().trim();
    state.filteredItems = state.items.filter(it => {
        const matchesSeries = state.currentSeries === 'All' || it.series === state.currentSeries;
        const matchesQuery = !q ||
            (it.title && it.title.toLowerCase().includes(q)) ||
            (it.series && it.series.toLowerCase().includes(q)) ||
            (it.item && it.item.toLowerCase().includes(q));
        return matchesSeries && matchesQuery;
    });
}

function updateVideoGrid() {
    const grid = document.getElementById('videoGrid');
    if (!grid) return;
    if (state.filteredItems.length === 0) {
        grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; color: var(--text-muted);">
                No videos found matching your criteria.
            </div>
        `;
    } else {
        grid.innerHTML = state.filteredItems.map(renderVideoCard).join('');
    }
}

function renderVideoCard(item) {
    const primaryVid = (item.video_ids && item.video_ids.length > 0) ? item.video_ids[0] : '';
    const thumbUrl = primaryVid ? `https://img.youtube.com/vi/${primaryVid}/mqdefault.jpg` : '';

    const langBadges = (item.languages || []).slice(0, 4).map(l => `
        <span class="lang-tag">${escapeHtml(l)}</span>
    `).join('');

    return `
        <div class="video-card" onclick="window.location.hash='#/item/${encodeURIComponent(item.id)}'">
            <div class="card-thumbnail">
                ${thumbUrl ? `<img src="${thumbUrl}" alt="${escapeHtml(item.title)}" loading="lazy">` : ''}
                ${item.parts_count > 1 ? `<span class="card-badge">${item.parts_count} parts</span>` : ''}
            </div>
            <div class="card-body">
                <span class="card-series">${escapeHtml(item.series)}</span>
                <h3 class="card-title">${escapeHtml(item.title)}</h3>
                <div class="card-footer">
                    <span>${item.has_transcript ? '📝 Transcript' : '✕ Audio only'}</span>
                    <div class="lang-tags">
                        ${langBadges}
                        ${item.languages && item.languages.length > 4 ? `<span class="lang-tag">+${item.languages.length - 4}</span>` : ''}
                    </div>
                </div>
            </div>
        </div>
    `;
}

async function renderItemView(itemKey) {
    const app = document.getElementById('app');
    app.innerHTML = `
        <div class="loading-state">
            <div class="spinner"></div>
            <p>Loading interactive transcripts & video...</p>
        </div>
    `;

    const manifestItem = state.items.find(i => i.id === itemKey);
    if (!manifestItem) {
        app.innerHTML = `
            <div class="loading-state">
                <h2>⚠️ Item Not Found</h2>
                <a href="#/" class="btn-back">← Back to Library</a>
            </div>
        `;
        return;
    }

    try {
        const resp = await fetch(manifestItem.data_url);
        if (!resp.ok) throw new Error('Failed to load item transcript data');
        state.currentItem = await resp.json();
        state.currentPartIndex = 0;
        state.currentLanguage = 'original';

        renderCurrentItemDOM();
    } catch (e) {
        app.innerHTML = `
            <div class="loading-state">
                <h2>⚠️ Error Loading Transcripts</h2>
                <p>${escapeHtml(e.message)}</p>
                <a href="#/" class="btn-back">← Back to Library</a>
            </div>
        `;
    }
}

function renderCurrentItemDOM() {
    const app = document.getElementById('app');
    const item = state.currentItem;
    const parts = item.parts || [];
    const currentPart = parts[state.currentPartIndex] || {};
    const videoId = currentPart.video_id || (parts.length > 0 ? parts[0].video_id : '');

    const translationLangs = Object.keys(item.translations || {});

    app.innerHTML = `
        <a href="#/" class="btn-back">← Back to Library</a>

        <div class="detail-view">
            <div class="player-panel">
                <div class="video-frame-container" id="ytPlayerContainer"></div>

                <div class="detail-header">
                    <h2 class="detail-title">${escapeHtml(item.title)}</h2>
                    <div class="detail-meta-row">
                        <span><strong>Series:</strong> ${escapeHtml(item.series)}</span>
                        ${item.episode ? `<span><strong>Episode:</strong> ${escapeHtml(item.episode)}</span>` : ''}
                        ${currentPart.duration ? `<span><strong>Duration:</strong> ${formatTime(currentPart.duration)}</span>` : ''}
                        ${currentPart.upload_date ? `<span><strong>Date:</strong> ${escapeHtml(currentPart.upload_date)}</span>` : ''}
                    </div>
                </div>
            </div>

            <div class="transcript-panel">
                <div class="panel-header">
                    <div class="panel-title">
                        <span>💬 Transcript</span>
                        ${parts.length > 1 ? `
                            <select class="part-selector" id="partSelector">
                                ${parts.map((p, idx) => `
                                    <option value="${idx}" ${idx === state.currentPartIndex ? 'selected' : ''}>
                                        Part ${idx + 1}: ${escapeHtml(p.title || p.video_id)}
                                    </option>
                                `).join('')}
                            </select>
                        ` : ''}
                    </div>

                    <select class="lang-selector" id="langSelector">
                        <option value="original" ${state.currentLanguage === 'original' ? 'selected' : ''}>
                            ${LANGUAGE_LABELS['original']}
                        </option>
                        ${translationLangs.map(l => `
                            <option value="${escapeHtml(l)}" ${state.currentLanguage === l ? 'selected' : ''}>
                                ${LANGUAGE_LABELS[l] || l}
                            </option>
                        `).join('')}
                    </select>
                </div>

                <div class="transcript-body" id="transcriptBody">
                    ${renderTranscriptCues()}
                </div>
            </div>
        </div>
    `;

    if (videoId) {
        createOrUpdatePlayer(videoId);
    }

    const partSel = document.getElementById('partSelector');
    if (partSel) {
        partSel.addEventListener('change', (e) => {
            state.currentPartIndex = parseInt(e.target.value, 10);
            renderCurrentItemDOM();
        });
    }

    const langSel = document.getElementById('langSelector');
    if (langSel) {
        langSel.addEventListener('change', (e) => {
            state.currentLanguage = e.target.value;
            const body = document.getElementById('transcriptBody');
            if (body) {
                body.innerHTML = renderTranscriptCues();
                attachCueClickListeners();
            }
        });
    }

    attachCueClickListeners();
}

function renderTranscriptCues() {
    const item = state.currentItem;
    if (!item) return '<p>No content available.</p>';

    if (state.currentLanguage !== 'original' && item.translations && item.translations[state.currentLanguage]) {
        const transList = item.translations[state.currentLanguage];
        const transObj = transList[state.currentPartIndex] || transList[0];
        if (!transObj || !transObj.cues || transObj.cues.length === 0) {
            return `<p class="text-muted">No translated cues available for this part.</p>`;
        }
        return transObj.cues.map((c) => `
            <div class="cue-row" data-start="${c.start}" data-end="${c.end}">
                <div class="cue-meta">
                    <span class="cue-time">⏱ ${formatTime(c.start)}</span>
                    <span class="cue-speaker">Translation (${escapeHtml(state.currentLanguage)})</span>
                </div>
                <div class="cue-text">${escapeHtml(c.text)}</div>
            </div>
        `).join('');
    }

    const currentTrans = (item.transcripts || [])[state.currentPartIndex] || (item.transcripts || [])[0];
    if (currentTrans && currentTrans.segments && currentTrans.segments.length > 0) {
        const speakersMap = (item.parts && item.parts[state.currentPartIndex] ? item.parts[state.currentPartIndex].speakers : null) || item.speakers || {};

        return currentTrans.segments.map(seg => {
            const speakerName = speakersMap[seg.speaker] || seg.speaker || 'Speaker';
            return `
                <div class="cue-row" data-start="${seg.start}" data-end="${seg.end}">
                    <div class="cue-meta">
                        <span class="cue-time">⏱ ${formatTime(seg.start)}</span>
                        <span class="cue-speaker">👤 ${escapeHtml(speakerName)}</span>
                    </div>
                    <div class="cue-text">${escapeHtml(seg.text)}</div>
                </div>
            `;
        }).join('');
    }

    if (item.raw_text) {
        return `
            <div style="white-space: pre-wrap; font-size: 0.9rem; line-height: 1.6; color: var(--text-primary);">
                ${escapeHtml(item.raw_text)}
            </div>
        `;
    }

    return `<p class="text-muted">No transcript available for this video.</p>`;
}

function attachCueClickListeners() {
    const cueRows = document.querySelectorAll('.cue-row');
    cueRows.forEach(row => {
        row.addEventListener('click', () => {
            const start = parseFloat(row.getAttribute('data-start'));
            if (!isNaN(start)) {
                seekToTime(start);
                cueRows.forEach(r => r.classList.remove('active'));
                row.classList.add('active');
            }
        });
    });
}

function highlightActiveCue(currentTime) {
    const cueRows = document.querySelectorAll('.cue-row');
    let activeRow = null;

    cueRows.forEach(row => {
        const start = parseFloat(row.getAttribute('data-start'));
        const end = parseFloat(row.getAttribute('data-end'));
        if (!isNaN(start) && !isNaN(end) && currentTime >= start && currentTime <= end) {
            activeRow = row;
        }
    });

    if (activeRow && !activeRow.classList.contains('active')) {
        cueRows.forEach(r => r.classList.remove('active'));
        activeRow.classList.add('active');

        const container = document.getElementById('transcriptBody');
        if (container) {
            const rowTop = activeRow.offsetTop - container.offsetTop;
            container.scrollTo({
                top: rowTop - 80,
                behavior: 'smooth',
            });
        }
    }
}

window.addEventListener('DOMContentLoaded', init);
