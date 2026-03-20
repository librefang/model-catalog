# Plugins

Plugin packages for LibreFang. Plugins extend agent behavior through lifecycle hooks -- they can inject memories, modify context, or perform side effects during conversations.

## Structure

```
plugins/
└── <plugin-name>/
    ├── plugin.toml          # Plugin manifest
    ├── hooks/
    │   ├── ingest.py        # Called on user message
    │   └── after_turn.py    # Called after each turn
    └── requirements.txt     # Python dependencies
```

## plugin.toml Format

```toml
name = "plugin-name"             # Must match directory name
version = "0.1.0"
description = "What this plugin does"
author = "author-name"

[hooks]
ingest = "hooks/ingest.py"       # Receives user message, can return memories
after_turn = "hooks/after_turn.py" # Post-turn processing
```

## Hook Protocol

Hooks communicate via stdin/stdout JSON:

### ingest hook

```
stdin:  {"type": "ingest", "agent_id": "...", "message": "user message"}
stdout: {"type": "ingest_result", "memories": [{"content": "..."}]}
```

### after_turn hook

```
stdin:  {"type": "after_turn", "agent_id": "...", "messages": [...]}
stdout: {"type": "ok"}
```

## Current Plugins (10)

| Plugin | Hooks | Description |
|--------|-------|-------------|
| auto-summarizer | ingest, after_turn | Running conversation summary for long context compression |
| context-decay | ingest, after_turn | Time-based memory decay with relevance scoring for natural forgetting |
| conversation-logger | after_turn | Logs conversations to JSONL files for auditing and analytics |
| episodic-memory | ingest, after_turn | Episode-based conversation segmentation and cross-session recall |
| guardrails | ingest | Safety filter detecting PII, prompt injection, and credential exposure |
| keyword-memory | ingest | Extracts keywords and named entities as contextual memories |
| sentiment-tracker | ingest | Analyzes user sentiment and injects emotional context |
| todo-tracker | ingest, after_turn | Detects, persists, and recalls action items from conversations |
| topic-memory | ingest, after_turn | Topic-aware keyword clustering with cross-conversation context recall |
| user-profile | ingest, after_turn | Persistent user profiling from conversation patterns for personalization |

## Adding a New Plugin

1. Create `plugins/<name>/plugin.toml`
2. Add hook scripts in `hooks/`
3. List dependencies in `requirements.txt` (prefer stdlib-only)
4. Run `python scripts/validate.py`
5. Submit a PR

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full guide.
