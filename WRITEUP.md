# Project Write-Up: Metasoftec Client Support Chatbot

## Use case chosen and why

**Client Support / Status Inquiry.** Out of the three candidate use cases (lead qualification, client support, quote drafting), this one was chosen because:
- It has a clear, bounded information need (project status), which makes it easy to ground the AI in real data instead of letting it improvise.
- It's a real, recurring task at Metasoftec — clients regularly ask "where are we?" and today that means someone manually checking and replying.
- It has natural, testable guardrails (pricing, dates, bugs) that make the refusal behavior easy to demonstrate and evaluate.

## Design decisions

1. **Grounding over memory.** The assistant is never allowed to answer from what it "knows" about a client — it's handed the client's JSON record fresh each time and instructed to treat it as the only source of truth. This is the main anti-hallucination technique in the project: if the record doesn't say it, the assistant doesn't say it either.

2. **Explicit allow/refuse lists.** Rather than a vague "be helpful," the prompt enumerates exactly what's in scope (phase, last update, next milestone, explaining the methodology) and exactly what isn't (pricing, uncommitted dates, bug fixes, other clients' data) — with a specific redirect for each refusal category, matching Metasoftec's real department split (Commercial, Technical).

3. **Tone matched to context.** The prompt asks for a professional but warm tone, and an Assalamualaikum greeting for Pakistani/Urdu-context clients — a small but real localization detail for Metasoftec's actual client base.

4. **Reusable packaging.** The same prompt logic is expressed three ways — a runnable CLI script, an Agent Skill (`SKILL.md`), and a slash command (`check-status.md`) — to show the prompt design is portable across different ways of invoking an AI assistant, not tied to one script.

## What the sample conversations demonstrate

See `sample-conversations.md`. Two in-scope answers show the assistant correctly using the record for both a direct status question and a "what does this phase mean" question. Four refusal cases show it consistently declining pricing, date-guarantee, bug-fix, and cross-client requests — each with an appropriate redirect rather than a flat "I can't help."

## Limitations and what I'd improve with more time

- **Static mock data.** `mock_clients.json` is hardcoded; a real version would query Metasoftec's live Odoo database via API so status is always current.
- **No identity verification.** Right now the client is just "selected" from a list. A real deployment needs to authenticate that the person asking is actually that client before returning any status.
- **Single-turn grounding.** The record is injected once at the start of the conversation; a longer-running chat should re-fetch it periodically in case status changes mid-conversation.
- **No escalation logging.** When the assistant redirects to Commercial/Technical, nothing is actually recorded or sent to those teams yet — a production version would trigger a real notification or ticket.

## Files in this repo

- `system_prompt.md` — the core prompt
- `mock_clients.json` — test data
- `support_chatbot.py` — runnable CLI demo
- `skills/client-support-assistant/SKILL.md` — same logic as a Claude Agent Skill
- `commands/check-status.md` — slash-command wrapper
- `sample-conversations.md` — evidence of correct in-scope and refusal behavior
- `README.md` — project overview and setup instructions
