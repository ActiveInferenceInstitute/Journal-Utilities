#!/usr/bin/env bash
# ============================================================================
# Journal-Utilities - Interactive Pipeline Orchestrator
# ============================================================================
# This script provides a unified interface for running the Journal-Utilities
# transcription and entity extraction pipelines with interactive API key setup.
# ============================================================================

set -euo pipefail

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${SCRIPT_DIR}/.env"
ENV_EXAMPLE="${SCRIPT_DIR}/.env.example"

# ============================================================================
# Utility Functions
# ============================================================================

print_header() {
    echo ""
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${NC}${BOLD}           Journal-Utilities Pipeline Orchestrator            ${NC}${BLUE}║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_section() {
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# ============================================================================
# Environment Setup Functions
# ============================================================================

ensure_env_file() {
    if [[ ! -f "$ENV_FILE" ]]; then
        if [[ -f "$ENV_EXAMPLE" ]]; then
            cp "$ENV_EXAMPLE" "$ENV_FILE"
            print_info "Created .env file from .env.example"
        else
            touch "$ENV_FILE"
            print_info "Created empty .env file"
        fi
    fi
}

get_env_value() {
    local key="$1"
    if [[ -f "$ENV_FILE" ]]; then
        grep -E "^${key}=" "$ENV_FILE" 2>/dev/null | cut -d'=' -f2- | sed 's/^["'"'"']//' | sed 's/["'"'"']$//' || echo ""
    else
        echo ""
    fi
}

set_env_value() {
    local key="$1"
    local value="$2"
    
    ensure_env_file
    
    # Remove existing key if present
    if grep -q "^${key}=" "$ENV_FILE" 2>/dev/null; then
        # Use different sed syntax for macOS vs Linux
        if [[ "$OSTYPE" == "darwin"* ]]; then
            sed -i '' "/^${key}=/d" "$ENV_FILE"
        else
            sed -i "/^${key}=/d" "$ENV_FILE"
        fi
    fi
    
    # Add new value
    echo "${key}=${value}" >> "$ENV_FILE"
}

is_key_configured() {
    local key="$1"
    local value
    value=$(get_env_value "$key")
    
    # Check if value exists and is not a placeholder
    if [[ -n "$value" ]] && \
       [[ "$value" != "your_"* ]] && \
       [[ "$value" != "YOUR_"* ]] && \
       [[ "$value" != *"_here" ]] && \
       [[ "$value" != *"_HERE" ]]; then
        return 0
    fi
    return 1
}

# ============================================================================
# API Key Configuration
# ============================================================================

declare -A API_KEYS=(
    ["HUGGINGFACE_TOKEN"]="Hugging Face Token (for speaker diarization)|https://huggingface.co/settings/tokens"
    ["API_KEY"]="YouTube Data API v3 Key (for video metadata)|https://console.developers.google.com/apis/"
    ["CODA_API_TOKEN"]="Coda API Token (for session data)|https://coda.io/account"
    ["COHERE_API_KEY"]="Cohere API Key (for entity extraction)|https://dashboard.cohere.com/api-keys"
)

# Optional keys that are nice to have but not required for basic operation
declare -A OPTIONAL_KEYS=(
    ["SURREALDB_PASSWORD"]="SurrealDB Password|Default: root"
)

check_api_keys() {
    print_section "Checking API Keys"
    
    local missing_keys=()
    local configured_keys=()
    
    for key in "${!API_KEYS[@]}"; do
        if is_key_configured "$key"; then
            configured_keys+=("$key")
            print_success "$key [configured]"
        else
            missing_keys+=("$key")
            print_error "$key [missing]"
        fi
    done
    
    echo ""
    
    if [[ ${#missing_keys[@]} -gt 0 ]]; then
        echo -e "${YELLOW}Some API keys are missing. Would you like to configure them now?${NC}"
        echo ""
        read -rp "Configure missing keys? [Y/n]: " response
        
        if [[ "$response" != "n" ]] && [[ "$response" != "N" ]]; then
            configure_missing_keys "${missing_keys[@]}"
        fi
    else
        print_success "All required API keys are configured!"
    fi
}

configure_missing_keys() {
    local keys=("$@")
    
    for key in "${keys[@]}"; do
        echo ""
        local info="${API_KEYS[$key]}"
        local description="${info%%|*}"
        local url="${info##*|}"
        
        echo -e "${BOLD}$description${NC}"
        echo -e "Get your key from: ${CYAN}$url${NC}"
        echo ""
        
        read -rp "Enter $key (or press Enter to skip): " value
        
        if [[ -n "$value" ]]; then
            set_env_value "$key" "$value"
            print_success "Saved $key to .env"
        else
            print_warning "Skipped $key"
        fi
    done
}

configure_all_keys() {
    print_section "Configure All API Keys"
    
    for key in "${!API_KEYS[@]}"; do
        echo ""
        local info="${API_KEYS[$key]}"
        local description="${info%%|*}"
        local url="${info##*|}"
        
        local current_value
        current_value=$(get_env_value "$key")
        
        echo -e "${BOLD}$description${NC}"
        echo -e "Get your key from: ${CYAN}$url${NC}"
        
        if is_key_configured "$key"; then
            echo -e "Current: ${GREEN}[configured]${NC}"
            read -rp "Enter new value (or press Enter to keep current): " value
        else
            echo -e "Current: ${RED}[not configured]${NC}"
            read -rp "Enter $key: " value
        fi
        
        if [[ -n "$value" ]]; then
            set_env_value "$key" "$value"
            print_success "Updated $key"
        fi
    done
    
    echo ""
    print_success "API key configuration complete!"
}

# ============================================================================
# Pipeline Operations
# ============================================================================

check_uv() {
    if ! command -v uv &> /dev/null; then
        print_error "uv is not installed. Please install it first:"
        echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
        exit 1
    fi
}

ensure_venv() {
    if [[ ! -d "${SCRIPT_DIR}/.venv" ]]; then
        print_info "Creating virtual environment..."
        cd "$SCRIPT_DIR" && uv sync
    fi
}

run_tests() {
    print_section "Running Tests"
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    uv run pytest tests/ -v
}

run_unit_tests() {
    print_section "Running Unit Tests (No Database Required)"
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    uv run pytest tests/journalrag/unit/ tests/journal_utilities/test_transcribe.py tests/journal_utilities/test_categorizer.py -v
}

start_database() {
    print_section "Starting SurrealDB"
    
    local db_path="${SCRIPT_DIR}/data/database"
    mkdir -p "$db_path"
    
    print_info "Starting SurrealDB at ws://localhost:8080..."
    surreal start --log info --user root --pass root --bind 0.0.0.0:8080 "rocksdb://${db_path}" &
    
    sleep 2
    print_success "Database started"
}

fetch_coda_data() {
    print_section "Fetching Data from Coda API"
    
    if ! is_key_configured "CODA_API_TOKEN"; then
        print_error "CODA_API_TOKEN is not configured"
        return 1
    fi
    
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    
    # Source .env to get the token
    set -a
    source "$ENV_FILE"
    set +a
    
    mkdir -p data/input
    curl -X GET "https://coda.io/apis/v1/docs/TwB_SP81yq/tables/grid-cjvFiXp3a3/rows?useColumnNames=true" \
        -H "Authorization: Bearer ${CODA_API_TOKEN}" \
        -o data/input/livestream_fulldata_table.json
    
    print_success "Data saved to data/input/livestream_fulldata_table.json"
}

import_sessions() {
    print_section "Importing Sessions to Database"
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    
    set -a
    source "$ENV_FILE"
    set +a
    
    uv run python -c "
import asyncio
import sys
sys.path.insert(0, 'src')
from journal_utilities.ingest_db_create_wav import insert_missing_sessions_from_json
import os

asyncio.run(insert_missing_sessions_from_json(
    'data/input/livestream_fulldata_table.json',
    os.getenv('DB_URL', 'ws://localhost:8080/rpc'),
    os.getenv('DB_USER', 'root'),
    os.getenv('DB_PASSWORD', 'root'),
    os.getenv('DB_NAME', 'actinf'),
    os.getenv('DB_NAMESPACE', 'actinf')
))
"
}

fetch_metadata() {
    print_section "Fetching YouTube Metadata"
    
    if ! is_key_configured "API_KEY"; then
        print_error "API_KEY (YouTube) is not configured"
        return 1
    fi
    
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    
    set -a
    source "$ENV_FILE"
    set +a
    
    cd src/journal_utilities && uv run python ingest_db_create_wav.py --step metadata
}

run_transcription() {
    print_section "Running Transcription Pipeline"
    
    if ! is_key_configured "HUGGINGFACE_TOKEN"; then
        print_error "HUGGINGFACE_TOKEN is not configured"
        return 1
    fi
    
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    
    set -a
    source "$ENV_FILE"
    set +a
    
    cd src/journal_utilities && uv run python transcribe.py
}

extract_entities() {
    print_section "Extracting Entities"
    
    if ! is_key_configured "COHERE_API_KEY"; then
        print_error "COHERE_API_KEY is not configured"
        return 1
    fi
    
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    
    set -a
    source "$ENV_FILE"
    set +a
    
    uv run python -m journalrag.main
}

copy_to_journal() {
    print_section "Copying to Journal Repository"
    check_uv
    ensure_venv
    cd "$SCRIPT_DIR"
    
    set -a
    source "$ENV_FILE"
    set +a
    
    cd src/journal_utilities && uv run python ingest_db_create_wav.py --step copy
}

run_full_pipeline() {
    print_section "Running Full Pipeline"
    
    echo "This will run the complete pipeline:"
    echo "  1. Fetch data from Coda"
    echo "  2. Import sessions to database"
    echo "  3. Fetch YouTube metadata"
    echo "  4. Run transcription"
    echo "  5. Extract entities"
    echo "  6. Copy to journal"
    echo ""
    read -rp "Continue? [Y/n]: " response
    
    if [[ "$response" == "n" ]] || [[ "$response" == "N" ]]; then
        return
    fi
    
    fetch_coda_data
    import_sessions
    fetch_metadata
    run_transcription
    extract_entities
    copy_to_journal
    
    print_success "Full pipeline complete!"
}

# ============================================================================
# Main Menu
# ============================================================================

show_menu() {
    print_section "Pipeline Operations"
    echo ""
    echo "  ${BOLD}Setup & Configuration${NC}"
    echo "    1) Check API keys"
    echo "    2) Configure all API keys"
    echo "    3) Install/update dependencies"
    echo ""
    echo "  ${BOLD}Database${NC}"
    echo "    4) Start SurrealDB"
    echo ""
    echo "  ${BOLD}Transcription Pipeline${NC}"
    echo "    5) Fetch data from Coda"
    echo "    6) Import sessions"
    echo "    7) Fetch YouTube metadata"
    echo "    8) Run transcription"
    echo "    9) Copy to journal"
    echo ""
    echo "  ${BOLD}Entity Extraction${NC}"
    echo "   10) Extract entities (Cohere AI)"
    echo ""
    echo "  ${BOLD}Full Pipeline${NC}"
    echo "   11) Run full pipeline"
    echo ""
    echo "  ${BOLD}Testing${NC}"
    echo "   12) Run all tests"
    echo "   13) Run unit tests only (no DB)"
    echo ""
    echo "    q) Quit"
    echo ""
}

main() {
    print_header
    check_uv
    ensure_env_file
    
    # Check for command line arguments
    if [[ $# -gt 0 ]]; then
        case "$1" in
            setup|configure)
                check_api_keys
                ;;
            test|tests)
                run_tests
                ;;
            unit-tests)
                run_unit_tests
                ;;
            transcribe)
                run_transcription
                ;;
            extract)
                extract_entities
                ;;
            full)
                run_full_pipeline
                ;;
            *)
                echo "Unknown command: $1"
                echo "Available commands: setup, test, unit-tests, transcribe, extract, full"
                exit 1
                ;;
        esac
        exit 0
    fi
    
    # Interactive menu
    while true; do
        show_menu
        read -rp "Select an option: " choice
        
        case "$choice" in
            1) check_api_keys ;;
            2) configure_all_keys ;;
            3) ensure_venv && print_success "Dependencies installed" ;;
            4) start_database ;;
            5) fetch_coda_data ;;
            6) import_sessions ;;
            7) fetch_metadata ;;
            8) run_transcription ;;
            9) copy_to_journal ;;
            10) extract_entities ;;
            11) run_full_pipeline ;;
            12) run_tests ;;
            13) run_unit_tests ;;
            q|Q) 
                echo ""
                print_info "Goodbye!"
                exit 0
                ;;
            *)
                print_error "Invalid option: $choice"
                ;;
        esac
        
        echo ""
        read -rp "Press Enter to continue..."
    done
}

# Run main function
main "$@"
