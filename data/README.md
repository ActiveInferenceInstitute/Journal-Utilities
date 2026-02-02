# Data Directory

Storage for database, input files, and processed outputs.

## Structure

```
data/
├── database/      # SurrealDB RocksDB storage
├── input/         # Source data files
│   └── livestream_fulldata_table.json  # Coda API export
└── output/        # Processed transcripts
    └── [session_name]/                  # Per-session outputs
        ├── [session_name].json          # Detailed transcript
        ├── [session_name]_simplified.json
        └── [session_name].txt           # Plain text transcript
```

## Folders

### `database/`

SurrealDB RocksDB storage. Contains all session metadata, transcription status, and extracted entities.

**Start database:**

```bash
surreal start --log trace --user root --pass root --bind 0.0.0.0:8080 rocksdb://./data/database
```

### `input/`

Source data from Coda API. Fetched with:

```bash
make fetch-coda
```

### `output/`

Transcribed sessions. Each session has:

- Full JSON with word-level timing
- Simplified JSON (without word arrays)
- Plain text transcript

## Maintenance

**Backup database:**

```bash
cp -r data/database data/database_backup
```

**Clear outputs:**

```bash
rm -rf data/output/*
```
