"""
Metasoftec Client Support Chatbot — student demo

Wires system_prompt.md + mock_clients.json together and runs a chat loop
against the Claude API for one selected client.

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY=your_key_here

Run:
    python support_chatbot.py
"""

import json
import os
import sys
from pathlib import Path

import anthropic

SCRIPT_DIR = Path(__file__).parent
SYSTEM_PROMPT_PATH = SCRIPT_DIR / "system_prompt.md"
CLIENTS_PATH = SCRIPT_DIR / "mock_clients.json"
MODEL = "claude-sonnet-4-6"


def load_system_prompt() -> str:
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def load_clients() -> list[dict]:
    return json.loads(CLIENTS_PATH.read_text(encoding="utf-8"))


def pick_client(clients: list[dict]) -> dict:
    print("Select a client:")
    for i, c in enumerate(clients, 1):
        print(f"  {i}. {c['client_name']}")
    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(clients):
            return clients[int(choice) - 1]
        print("Invalid choice, try again.")


def build_system_message(base_prompt: str, client_record: dict) -> str:
    return (
        f"{base_prompt}\n\n"
        "## Current client record (only source of truth for this conversation)\n"
        f"{json.dumps(client_record, indent=2)}"
    )


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("Set ANTHROPIC_API_KEY before running.")

    client_sdk = anthropic.Anthropic(api_key=api_key)
    base_prompt = load_system_prompt()
    clients = load_clients()
    selected = pick_client(clients)
    system_message = build_system_message(base_prompt, selected)

    print(f"\nChatting as support assistant for {selected['client_name']}.")
    print("Type 'quit' to exit.\n")

    history = []
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            break
        history.append({"role": "user", "content": user_input})

        response = client_sdk.messages.create(
            model=MODEL,
            max_tokens=500,
            system=system_message,
            messages=history,
        )
        reply = "".join(
            block.text for block in response.content if block.type == "text"
        )
        print(f"Assistant: {reply}\n")
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
