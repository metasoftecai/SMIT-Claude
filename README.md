# Metasoftec Client Support Chatbot

A small, grounded AI chatbot that answers Metasoftec clients' questions about their own Odoo ERP implementation status — built as a Module 1 (prompt engineering) project using Metasoftec as the real-world case study.

## Use case

Client Support / Status Inquiry: instead of a client emailing Metasoftec to ask "what phase is my project in?", this assistant answers instantly from the client's own project record — and refuses anything outside its scope (pricing, date commitments, technical bug fixes), redirecting to the right team instead.

## How it works

1. A **system prompt** (`system_prompt.md`) defines the assistant's role, knowledge boundaries, allowed topics, and refusal rules.
2. A **mock dataset** (`mock_clients.json`) stands in for real client records — current phase, last update, next milestone — so the bot never invents status information.
3. A **runner script** (`support_chatbot.py`) loads the prompt + a selected client's record, injects the record as grounding context, and runs a live chat loop against the Claude API.
4. A **packaged Agent Skill** (`skills/client-support-assistant/SKILL.md`) turns the same logic into a reusable Claude Skill that other tools (like Claude Code or Claude Desktop) can trigger automatically.
5. A **slash command** (`commands/check-status.md`) gives a one-line way to invoke it: `/check-status <client name>`.

## Why this design

- **Grounding over memory** — the model is never trusted to "remember" a client's status; it's handed the exact record each time, which is the core anti-hallucination technique this project demonstrates.
- **Explicit refusals** — the prompt lists what the assistant must NOT do, and hands those cases off to the right Metasoftec team (Commercial, Technical), matching how Metasoftec's real departments are structured.
- **Reusability** — packaging the same logic as both a script and a Skill shows the same prompt can power a CLI demo *and* be dropped into an agentic tool.

## Files

| File | Purpose |
|---|---|
| `system_prompt.md` | Core system prompt / persona definition |
| `mock_clients.json` | Sample client status records for testing |
| `support_chatbot.py` | Runnable CLI chatbot (Claude API) |
| `skills/client-support-assistant/SKILL.md` | Same assistant packaged as a Claude Agent Skill |
| `commands/check-status.md` | Slash-command wrapper for quick invocation |

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
python support_chatbot.py
```

## What's next / limitations

- `mock_clients.json` is fake data — a production version would query Metasoftec's actual Odoo database via API.
- No authentication layer — a real deployment would need to verify the client's identity before returning any status.
- Single-turn grounding only — a production version would refresh the client record on each turn in case status changes mid-conversation.

Built for Metasoftec (metasoftec.com) — Karachi-based Odoo ERP implementation consultancy.
