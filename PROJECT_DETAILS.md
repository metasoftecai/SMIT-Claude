# Project Details — Metasoftec Client Support Chatbot

**Author:** Muhammed Saeed
**Company:** Metasoftec (Odoo ERP Consulting), Karachi, Pakistan — www.metasoftec.com
**Module:** Module 1 — Prompt Engineering / AI Tool Build
**Repo:** https://github.com/metasoftecai/SMIT-5/tree/main/client-support-chatbot

---

## 1. Overview

A small, spec-driven AI chatbot built for Metasoftec that answers a client's questions about their own Odoo ERP implementation status — current phase, last update, and next milestone — grounded strictly in that client's project record. It refuses and redirects anything outside status inquiry (pricing, undated commitments, technical bugs), matching how Metasoftec's real departments (Commercial, Technical) are structured.

## 2. Company background

Metasoftec is an Odoo ERP consulting and implementation company founded in 2022, headquartered in Karachi, Pakistan. It delivers the full ERP lifecycle — business analysis, implementation, data migration, customization, training, integration, and support — for clients across Pakistan, Canada, the UAE, Somalia, Djibouti, Kenya, and other markets, serving industries including retail, manufacturing, healthcare, education, construction, and logistics.

## 3. Use case selected

**Client Support / Status Inquiry** — chosen over lead qualification and quote drafting because it has a clear, bounded information need (project status) that's easy to ground in real data, is a genuine recurring task at Metasoftec today (clients ask "where are we?" via email/WhatsApp and someone manually replies), and has natural, testable refusal boundaries.

## 4. Project structure (creation order)

Built spec-first: the spec defines requirements and acceptance criteria, then the prompt, data, code, and packaging layers are built to satisfy it, followed by evidence and documentation.

| Sr # | File | Role |
|---|---|---|
| 1 | `specs/client-support-assistant.spec.md` | Requirements (F1–F8, N1–N3) and acceptance criteria |
| 2 | `system_prompt.md` | Core system prompt / persona |
| 3 | `mock_clients.json` | Test data — 5 sample client project records |
| 4 | `support_chatbot.py` | Runnable CLI chatbot (Claude API) |
| 5 | `skills/client-support-assistant/SKILL.md` | Same logic packaged as a reusable Claude Agent Skill |
| 6 | `commands/check-status.md` | Slash command: `/check-status <client name>` |
| 7 | `.claude/agents/client-support-assistant.md` | Claude Code subagent for automatic delegation |
| 8 | `sample-conversations.md` | 6 transcripts demonstrating correct grounded answers + refusals |
| 9 | `WRITEUP.md` | Design decisions, what the samples demonstrate, limitations |
| 10 | `README.md` | Top-level project overview and setup instructions |

## 5. How it works

1. A client is identified and their JSON record (phase, last update, next milestone) is loaded from `mock_clients.json`.
2. That record is injected into the system prompt as the **only source of truth** — the assistant is instructed never to invent or assume status details.
3. The assistant answers status questions and explains Metasoftec's 10-step methodology (Business Requirement Analysis → Gap Analysis → Solution Design → System Configuration → Custom Development → Data Migration → UAT → User Training → Go-Live Support → Continuous Improvement) in plain language.
4. Anything outside scope — pricing, uncommitted dates, technical bugs, another client's data — is refused with a specific redirect to the right Metasoftec team.

## 6. Design decisions

- **Grounding over memory** — the model never answers from what it "knows"; it's handed the exact record each time. This is the core anti-hallucination mechanism.
- **Explicit allow/refuse lists** — rather than a vague "be helpful," the prompt enumerates in-scope topics and refusal categories, each redirected to a specific Metasoftec team (Commercial, Technical).
- **Localized tone** — professional and warm, with "Assalamualaikum" as the greeting for Urdu/Pakistani-context clients, matching Metasoftec's actual client base.
- **Reusable packaging** — the same prompt logic is expressed four ways: standalone script, Agent Skill, slash command, and Claude Code subagent — proving the design generalizes rather than being tied to one script.

## 7. Testing

- **Structural tests** (see repo commit history) verify: the system prompt loads and contains refusal rules; all 5 client records load with required fields; the grounded context for a selected client contains only that client's data (no cross-client leakage).
- **Behavioral evidence** (`sample-conversations.md`) demonstrates 2 in-scope answers and 4 correct refusals (pricing, uncommitted date, technical bug, cross-client question), each mapped back to a specific acceptance criterion in the spec.

## 8. Setup & running

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
python support_chatbot.py
```

Select a client from the prompted list, then chat. Type `quit` to exit.

## 9. Limitations and future improvements

- `mock_clients.json` is static test data; production would query Metasoftec's live Odoo database via API.
- No client identity verification/authentication before returning status.
- Grounding happens once per conversation, not re-fetched mid-conversation if status changes.
- Refusal redirects aren't yet logged or ticketed to the Commercial/Technical teams — currently just stated to the client.

## 10. File index

```
client-support-chatbot/
├── specs/client-support-assistant.spec.md
├── system_prompt.md
├── mock_clients.json
├── support_chatbot.py
├── skills/client-support-assistant/SKILL.md
├── commands/check-status.md
├── .claude/agents/client-support-assistant.md
├── sample-conversations.md
├── WRITEUP.md
├── README.md
└── PROJECT_DETAILS.md   (this file)
```
