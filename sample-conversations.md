# Sample Conversations — Client Support Assistant

These transcripts demonstrate the assistant answering from its client record, and correctly refusing out-of-scope requests. Generated using the system prompt + client records in this repo.

---

## 1. In-scope: status check (Ramadan Corporation)

**Client record used:** Ramadan Corporation — Phase: System Configuration

> **Client:** Hi, can you tell me where my project stands right now?
>
> **Assistant:** Assalamualaikum! Your project, the Odoo 17 Configuration Audit & Rollout, is currently in the **System Configuration** phase. As of September 10, we've finalized your Chart of Accounts and taxes, and we're now working through the inventory module configuration. Next up is **Data Migration kickoff**, targeted for September 22. Let me know if you'd like more detail on any part of it.

---

## 2. In-scope: explaining a phase (Al Faiz Builders)

**Client record used:** Al Faiz Builders — Phase: Data Migration

> **Client:** What actually happens during "Data Migration"? Is that almost done?
>
> **Assistant:** Data Migration is when we move your historical business data — invoices, vendor bills, inventory records, etc. — from your old system (QuickBooks, in your case) into Odoo. For your project, we've already migrated historical invoices and vendor bills. What's still pending is your bank reconciliation data, which we're waiting on you to upload. Once that's in, we'll move to **User Acceptance Testing**, targeted for September 25.

---

## 3. Out-of-scope: pricing (Bethak School Network)

**Client record used:** Bethak School Network — Phase: User Training

> **Client:** Since we're almost done, can you give us a discount on the go-live support phase?
>
> **Assistant:** That's something our Commercial team handles directly — I can flag it for them, or you can reach us at www.metasoftec.com. On the project side, your admin and finance staff have completed training, and your branch coordinators' session is scheduled next, ahead of Go-Live Support.

*(Correctly redirects pricing instead of negotiating or inventing a discount.)*

---

## 4. Out-of-scope: uncommitted date (Moumin Group)

**Client record used:** Moumin Group — Phase: Custom Development

> **Client:** Can you guarantee the connector will be fully live by next Monday?
>
> **Assistant:** I can't guarantee a specific date beyond what's confirmed — right now the connector is in active development and internal testing, with User Acceptance Testing targeted for October 5. Our project team will confirm the go-live date once UAT is underway. I'll flag your question so they can follow up directly.

*(Refuses to commit to a date not present in the record, rather than guessing "yes.")*

---

## 5. Out-of-scope: technical bug (Pie In the Sky)

**Client record used:** Pie In the Sky — Phase: Continuous Improvement

> **Client:** One of our stock reports is showing the wrong quantity, can you fix it?
>
> **Assistant:** That needs our Technical Support team — I can flag this for them, or you can reach us at www.metasoftec.com. What I can tell you is you're currently live on Odoo with ongoing automation and stock reporting enhancements in progress, with the next review set for October 1.

*(Refuses to diagnose/fix a live bug, redirects appropriately.)*

---

## 6. Out-of-scope: cross-client question (any client)

> **Client:** How is Al Faiz Builders' project going compared to mine?
>
> **Assistant:** I'm only able to discuss your own project's status, not other clients' — happy to give you a full update on yours, though.

*(Refuses to leak another client's data.)*
