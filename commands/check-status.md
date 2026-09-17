---
description: Check a Metasoftec client's project status using the Client Support Assistant skill
argument-hint: <client name>
---

Look up the client record for "$ARGUMENTS" in `mock_clients.json` (or the real Odoo client data source if connected).

If found, use the `client-support-assistant` skill to answer as if the client themselves asked: "What's the status of my project?" — reporting current phase, last update, and next milestone in the assistant's defined tone.

If not found, say the client record isn't available and offer to connect them with Metasoftec at www.metasoftec.com rather than guessing.

Do not invent any status details not present in the record.
