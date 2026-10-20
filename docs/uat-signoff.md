# UAT sign-off sheet

**System:** Academic Document Generation & Validation System (MVP: TOR and COE)
**Scope:** MVP specification Section 19. Test details are in [test-plan.md](test-plan.md).
**Environment:** server URL ______________________  Scan station: ______________________
**UAT date(s):** ______________________

Mark each line **P** (Pass) or **F** (Fail). Any Fail needs a remark and a fix date. "VALID" means the printed information matches the school's records. It does not certify that the paper is authentic.

## A. Use cases (Section 22)

| # | Use case | Needs scanner? | P / F | Remarks |
| --- | --- | --- | --- | --- |
| UC1 | Student requests a TOR. Eligibility passes and the request goes to For Approval. An INC grade is rejected with the reason shown. A duplicate request is blocked. | No | | |
| UC2 | Registrar reviews side by side and approves, and the document is released. Reject with a reason, then regenerate, issues a new document number. Revoke works. | No | | |
| UC3 | Student downloads and prints at 100%. The download is logged. An expired window can be re-opened by the registrar. | No | | |
| UC4 | Operator scans in Single mode. Pages feed and the paper goes to the single tray. A jam is shown and the run resumes. | **Yes** | | |
| UC5 | Genuine document gives **VALID** with every field matching. A covered QR gives NEEDS REVIEW. | **Yes** | | |
| UC6 | Altered grade gives **INVALID** with printed vs official values and the image crop. An unclear alteration gives NEEDS REVIEW, which the registrar resolves. | **Yes** | | |
| UC7 | Bulk stack of 20: split by document, batch table, totals, export. A missing page gives INVALID with the page named. | **Yes** | | |

## A2. Records, accounts and audit (Sections 4, 5A–5C, 5H)

| # | Feature | Needs scanner? | P / F | Remarks |
| --- | --- | --- | --- | --- |
| S1 | **Academic setup:** add a term and make it current; add programs, subjects and teachers; create a class section, assign its teacher, and enroll a class list by student number. An unknown or already-enrolled number stops the whole list, with every problem shown. | No | | |
| S2 | **CSV/Excel imports:** import students from the template file. A file with errors imports nothing and lists every bad row. A teacher imports grades for their own section. | No | | |
| S3 | **Grade change approval:** after the term is locked, the teacher requests a change with a reason. The registrar sees it in the approval queue (student, subject, old and new grade) and approves it (the grade changes) or rejects it (the grade stays). | No | | |
| S4 | **Audit trail search:** find events by text (e.g. a document number or email), action and date range; open the timeline of one document from request to scan. Students and teachers cannot open it. | No | | |
| S5 | **Password reset and unlock:** five wrong passwords lock an account; it unlocks by itself after 15 minutes, or at once when the registrar (students, teachers) or admin resets the password, which forces a new password at the next sign-in. | No | | |

## B. Demo scenario (Section 23)

| # | Step | P / F | Remarks |
| --- | --- | --- | --- |
| 1 | Registrar creates student "Maria Santos". Account and audit entry appear. | | |
| 2 | Teacher encodes grades. Registrar locks the term, and edits are then blocked. | | |
| 3 | Upload the TOR template, preview with Maria's data, activate. | | |
| 4 | Maria requests a TOR. Status For Approval. | | |
| 5 | TOR generated with document number and QR in under 10 s. | | |
| 6 | Registrar approves. Released on Maria's dashboard. | | |
| 7 | Print the TOR. | | |
| 8 | Scan in Single mode. Paper goes to the single tray. *(scanner)* | | |
| 9 | Extracted fields shown with confidence. *(scanner)* | | |
| 10 | Every field matches. *(scanner)* | | |
| 11 | Green **VALID**, "matches official records". *(scanner)* | | |
| 12 | Alter a printed copy (edited PDF, or tape and handwriting). | | |
| 13 | Scan the altered copy. *(scanner)* | | |
| 14 | Grade highlighted: printed vs official, with crop. *(scanner)* | | |
| 15 | Red **INVALID** (or NEEDS REVIEW if unclear). *(scanner)* | | |
| 16 | Fake TOR with a made-up number gives **INVALID**, "not issued by this institution". *(scanner)* | | |
| 17 | Bulk stack of 5 (3 genuine, 1 altered, 1 fake) gives 3 VALID, 2 INVALID. *(scanner)* | | |
| 18 | Audit trail for Maria's TOR, from request to both scans (timeline on the request review screen). | | |

## C. Go-live checks

| Check | P / F | Remarks |
| --- | --- | --- |
| OCR accuracy ≥ 98% on ≥ 100 scanned documents (test-plan Section 5) | | |
| Tamper set: zero altered documents VALID (test-plan Section 6) | | |
| Security scan: no critical or high findings (test-plan Section 7; CI scan had 0 High) on the school server | | |
| Backup restore tested on the school server with `verify-backup.sh` (test-plan Section 8; already passed in CI) | | |
| Backups written to off-server storage; backup passphrase stored safely away from the server | | |
| Scan station starts the agent with `--delete-after-upload` (file-drop mode) and `--ca-cert` if the certificate is a campus one | | |
| HTTPS on all traffic, including the scan station | | |

## D. Known limitations and open items at sign-off

1. **Official templates pending.** The TOR and COE use stand-in layouts and placeholder school details (name, address, signatory) until the school supplies its official formats (Section 28 Q14). OCR zones must be re-checked when the official templates arrive.
2. **Client answers pending.** Section 28 questions, especially Q1–7 (documents in scope, SIS, forgery expectations, QR approval, legal CTC standing, output trays, legacy data) and Q22–23 (DPO, retention periods).
3. **Scanner hardware pending.** The TWAIN/SANE scanner driver, jam and double-feed detection, enclosure and trays are in progress (Daniel). Until then scanning runs in file-drop mode, and every step marked "Needs scanner" or *(scanner)* can only be accepted on the installed station.
4. **Not yet implemented:** the logo/layout check (Section 8, Level 2). It is blocked until the school supplies its official templates and logo. Validation already checks the QR code, document number, page count, page markers, the footer reference and every printed field. See test-plan Section 9.
5. **Privacy:** the DPO decisions in [privacy-data-inventory.md](privacy-data-inventory.md) Section 7 are open. The production station must run with `--delete-after-upload`; after an interrupted run, the operator resumes it or clears the drop folder by hand.
6. **Out of MVP scope (by agreement):** signature, stamp and seal verification; image forensics; legal recognition as a CTC replacement; COG, COR and Diploma.

## E. Decision

☐ Accepted  ☐ Accepted with the open items above  ☐ Not accepted (see remarks)

Remarks: ____________________________________________________________________

## F. Signatures

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Registrar | | | |
| School representative | | | |
| Development team: software | JC (Juan Carlos Gan) | | |
| Development team: hardware | Daniel (Daniel Rein Cosare) | | |
