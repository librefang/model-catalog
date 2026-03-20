#!/usr/bin/env python3
"""Echo memory after_turn hook — demo plugin.

Logs the number of messages in the conversation after each turn.

Receives via stdin:
    {"type": "after_turn", "agent_id": "...", "messages": [...]}

Prints to stdout:
    {"type": "ok"}
"""
import json
import sys


def main():
    request = json.loads(sys.stdin.read())
    agent_id = request.get("agent_id", "unknown")
    messages = request.get("messages", [])

    # In a real plugin you might update an index or persist state here.
    # For this demo we just acknowledge.
    print(json.dumps({"type": "ok"}), flush=True)


if __name__ == "__main__":
    main()
