# Demo script (Section 23, about 25 minutes)

For the presenters: JC (software) drives the web app; Daniel (hardware) runs the scan station.
Every step lists the screen, the click path and what the client should notice. Steps 7–8 and
12–13 need the printer and scanner; each has a fallback so the demo never stalls.

## Before the day (checklist)

- [ ] Server running (`docker compose ps` all healthy) or, for an offline demo, the laptop dev
      launcher (`backend/scripts/dev_server.py` + `npm run dev`, see README).
- [ ] Demo data loaded: on a laptop server the Section 23 set (1 program, 8 subjects over 2
      terms, 3 students); on a production server only the removable SAMPLE set (see
      [Demo data](#demo-data-sample-removable)), never the Section 23 set.
- [ ] Demo accounts signed in once and passwords changed (registrar, teacher, Maria, admin);
      write the new passwords on the presenter sheet, not on slides.
- [ ] Scan station registered; agent running in `--watch` mode (shows **● Ready · Waiting for paper**); `--ca-cert` set; feeder and both trays empty.
- [ ] Printer loaded with A4, set to **100% scale / actual size** (never "fit to page").
- [ ] Prepared paper, in labelled folders: a genuine Maria TOR printed the day before; an edited-PDF
      copy (IT101 changed to 1.00); a correction-tape copy; a fake TOR with a made-up number
      (`TOR-2026-424242`); the 5-document bulk stack (3 genuine, 1 altered, 1 fake).
- [ ] Fallback folder on the station PC with scans of every prepared sheet (file-drop mode).
- [ ] Browser zoom 125% on the projector; four browser profiles (registrar, teacher, student, operator).

## The run

| # | Min | Screen and clicks | Say / point out |
| --- | --- | --- | --- |
| 1 | 0:00 | Registrar → **Records → Add student**: Maria Santos, number, BSIT, login email + temporary password → **Add student**. Then **Audit trail**, search "maria" | Account and profile created; the audit entry appears with who, when and from where |
| 2 | 2:00 | Teacher → **My classes → IT101** → enter grades → **Save** → **Submit grades as final**. Registrar → **Academic setup → Lock grades** for the term | A wrong entry (e.g. 4.00) is flagged on its row and nothing saves. After locking, the teacher can only **Request change** |
| 3 | 5:00 | Registrar → **Templates → New version** → **Save as new draft** → **Preview PDF** → **Activate** | "All checks pass": unknown or missing placeholders would block activation. The preview is filled with real data |
| 4 | 7:00 | Maria (phone-size browser) → **Request a document**: TOR, purpose "Employment" → **Submit** | Only document types she is eligible for are offered. Status is *Pending* immediately (registrar approval first) |
| 5 | 8:00 | Registrar → **Dashboard → Approval queue → REQ-…** → **Approve request** | Nothing was generated before approval; now the PDF is generated (under 10 s) with document number, QR code and the reference in the footer. Maria sees *Approved* |
| 6 | 9:00 | Same page (or **Verification queue**): compare **Check against records**, then **Verify & release** | Side-by-side check; Maria's request shows *Completed* and **Download PDF** with the expiry date |
| 7 | 10:00 | Maria → **Download PDF** → print at 100% | *Fallback:* use the genuine TOR printed the day before |
| 8 | 11:00 | Operator → **Scan station → Single document**; Daniel feeds the page | Dashboard names the **SINGLE** tray. *Fallback:* run the agent on the fallback folder |
| 9–11 | 12:00 | Result appears (within 15 s) | Large green **VALID**: "Information matches official records as of …". Every field listed with OCR confidence |
| 12 | 14:00 | Show the altered copies (edited PDF; correction tape with a handwritten or overprinted 1.00) | Real tampering looks like this |
| 13–15 | 15:00 | **Single document** again, scan the altered copy | Red **INVALID**: IT101 printed 1.00 vs official 1.25, with the scanned row shown under it. If the overprint is unclear: amber **NEEDS REVIEW**; open it and decide with remarks |
| 16 | 18:00 | Scan the fake TOR | **INVALID**: "Document not issued by this institution" |
| 17 | 19:00 | **Bulk stack**, feed all 5 | Batch table fills live: 3 VALID, 2 INVALID, each with its stack position. **PDF** export of the batch |
| 18 | 22:00 | Registrar → **Requests → Maria's TOR → History (audit trail)** | Full history from request, approval, generation, verification and download to every scan and its result |
| — | 23:00 | Questions | Keep the Section 15 wording: VALID means *matches official records*, never "authentic" |

## If something goes wrong

| Problem | Do this |
| --- | --- |
| Scanner jams | Dashboard shows "Paper jam". Clear it, then re-run the agent with `--start-sequence` from the sheet it names; the session continues |
| Scanner not detected | Copy the matching scans from the fallback folder into the watched scanner folder: same results, same screens |
| Station shows Offline | Operator buttons are disabled on purpose. Reconnect the USB, wait for "Ready" |
| Printer problem | Use the pre-printed genuine copy |
| Network down | Run the laptop dev launcher; the scan agent points to `http://127.0.0.1:8000` |
| A result is NEEDS REVIEW instead of VALID | That is the system being careful (e.g. low OCR confidence). Open it, show the reason and the crop, confirm with remarks |

## Demo data (SAMPLE, removable)

A server that will later hold real student records (production) gets only the SAMPLE set. It
is created through the API's own routes (real rules, audit entries, document numbers and
hashes), every name or code in it contains `SAMPLE`, and every account uses
`@demo.school.edu.ph`. Run the commands from a PC with the backend installed (`cd backend`,
virtual environment active), with `ADGVS_DATABASE_URL` set to the API's database login and,
for a cloud server, the same storage settings as the API (`ADGVS_STORAGE_BACKEND`,
`ADGVS_SUPABASE_URL`, `ADGVS_SUPABASE_SERVICE_KEY`, `ADGVS_STORAGE_BUCKET`).

1. **Seed** (safe to repeat: only missing parts are added):

   ```bash
   python -m app.manage seed-demo --api https://<api-host> --password-file demo-accounts.txt
   ```

   Creates a SAMPLE program with 8 subjects over 2 terms (the older one locked), 8 class
   sections, a teacher and a class adviser, a registrar with the validation permission, 4
   students with grades, 4 document requests (released, for verification, pending, rejected by
   the eligibility rules) and the station **SAMPLE Demo Intake Station**. Passwords and the
   station key are random and shown once (here: written to the file; keep it out of the
   repository and delete it after the demo). `--api` lets the server render the PDFs; without
   it, a PC that cannot render PDFs leaves two requests Pending and says so. Lost a password:
   `--reset-passwords`.

2. **Feed SAMPLE documents through screening** (simulated camera station, real screening and
   backend decision):

   ```bash
   cd scan-agent
   python -m scan_agent intake-demo --server https://<api-host> --key <station key>
   ```

   Seven pages about one invented learner surnamed SAMPLE: a clean page of each of the four
   document types, a tampered good moral certificate, a memo and a poor capture. It prints, per
   page, the type read, the decision (passed screening / needs manual review), the tray and the
   reason codes. The same `--seed` gives the same pages; `--count N` changes the batch size.
   When creating a student profile from one of these documents, use a student number that
   starts with `SAMPLE-` (the learner's surname already marks it).

3. **Purge** after the demo:

   ```bash
   python -m app.manage purge-demo --dry-run   # what would be removed
   python -m app.manage purge-demo             # asks you to type PURGE
   ```

   Removes the SAMPLE records, every request, document and intake document of a SAMPLE student,
   all documents of the SAMPLE station (and the station itself), the generated PDFs and page
   images in storage. `--include-station NAME` also removes the intake documents and scan
   sessions of another station that scanned SAMPLE paper (the station stays). It stops without
   changing anything if a real record depends on SAMPLE data, or if the stored files are not in
   the storage it is configured for (wrong storage settings would orphan them). Not removable by design: audit
   entries (append-only; demo entries stay, identifiable by `@demo.school.edu.ph` accounts and
   SAMPLE values between the `demo_data_seeded` and `demo_data_purged` entries) and the demo
   accounts themselves (the audit trail references them: they are deactivated, given an
   unusable password and renamed `purged-<id>-...@demo.school.edu.ph`). Destroy printed SAMPLE
   documents: a later real document may reuse their number.

## Rehearsal record

| Date | Who | Duration | Steps done | Issues found |
| --- | --- | --- | --- | --- |
| 2026-10-05 | JC (software only, dev launcher, production security headers) | not timed | 3 (preview), 4–6, 9–11 and 13–15 with file-drop images, 18; plus grade change request → approval, offline-scanner block | Fixed during the run: loading states shown as "empty". Not yet run end to end: 1, 2, 16, 17 (done in earlier testing), 7–8 (need printer and scanner) |
| | JC + Daniel (full, timed) | | | |
| | JC + Daniel (full) | | | |
