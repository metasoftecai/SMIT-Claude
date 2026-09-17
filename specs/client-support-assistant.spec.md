# Spec: Client Support / Status Inquiry Assistant

## Problem

Metasoftec clients currently ask project-status questions ("what phase are we in?", "when is go-live?") via email or WhatsApp, requiring manual lookup and reply from the project team. This creates response delay and repeats the same low-complexity question across many clients.

## Goal

An AI assistant that answers a client's own project-status questions instantly and accurately, using their project record as the only source of truth, while refusing and redirecting anything outside status inquiry (pricing, undated commitments, technical bugs).

## Non-goals

- Not a general Odoo support/bug-fixing assistant.
- Not a pricing or negotiation tool.
- Not a replacement for human project managers — only handles status lookup.

## Requirements

### Functional

| ID | Requirement |
|---|---|
| F1 | Given a client identifier, the assistant retrieves that client's current project record. |
| F2 | The assistant answers questions about current phase, last update, and next milestone using only fields present in the record. |
| F3 | The assistant explains what a given phase means using Metasoftec's 10-step methodology. |
| F4 | If no record exists for the requested client, the assistant states this and does not fabricate one. |
| F5 | The assistant refuses pricing/discount requests and redirects to the Commercial team. |
| F6 | The assistant refuses to commit to any date not explicitly present in the record. |
| F7 | The assistant refuses technical/bug-fix requests and redirects to Technical Support. |
| F8 | The assistant refuses to disclose or compare another client's project data. |

### Non-functional

| ID | Requirement |
|---|---|
| N1 | Tone is professional, warm, concise; no markdown headers in chat replies. |
| N2 | Greets with "Assalamualaikum" for Urdu/Pakistani-context clients. |
| N3 | Logic must be reusable across at least three invocation surfaces (script, Skill, subagent/command) without rewriting the core prompt. |

## Acceptance criteria

- [ ] For each of the 5 sample clients, a status question returns the correct phase, last update, and next milestone (see `sample-conversations.md`).
- [ ] A pricing question is refused and redirected to Commercial (not answered with a number).
- [ ] A date-guarantee question beyond what's in the record is refused, not affirmed.
- [ ] A bug-fix request is redirected to Technical Support, not attempted.
- [ ] A cross-client question is declined.
- [ ] The same prompt logic runs successfully as: a CLI script, an Agent Skill, and a Claude Code subagent/command.

## Out of scope for this version

- Live Odoo database integration (uses static mock data instead — see `mock_clients.json`).
- Client identity verification/authentication.
- Escalation logging/ticket creation when a refusal redirect happens.

## Traceability

| Requirement | Implemented in |
|---|---|
| F1–F4 | `system_prompt.md`, `support_chatbot.py`, `mock_clients.json` |
| F5–F8 | `system_prompt.md` (refusal rules) |
| N1–N2 | `system_prompt.md` (tone section) |
| N3 | `skills/client-support-assistant/SKILL.md`, `commands/check-status.md`, `.claude/agents/client-support-assistant.md` |
| Acceptance criteria | `sample-conversations.md` |
