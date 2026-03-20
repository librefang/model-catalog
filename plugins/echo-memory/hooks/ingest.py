#!/usr/bin/env python3
"""Echo memory ingest hook — demo plugin.

Echoes the user message back as a "recalled memory" to verify
the plugin system works end-to-end.

Receives via stdin:
    {"type": "ingest", "agent_id": "...", "message": "user message text"}

Prints to stdout:
    {"type": "ingest_result", "memories": [{"content": "..."}]}
"""
import json
import sys


def main():
    request = json.loads(sys.stdin.read())
    message = request.get("message", "")
    agent_id = request.get("agent_id", "unknown")

    memories = [
        {"content": f"[echo-memory] Agent {agent_id} received: {message[:200]}"}
    ]

    result = {"type": "ingest_result", "memories": memories}
    print(json.dumps(result))


if __name__ == "__main__":
    main()
