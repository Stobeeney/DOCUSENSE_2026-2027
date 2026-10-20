# Academic Document Generation & Validation System
## Information we need from the school

**Date:** October 8, 2026
**Demo / go-live target:** October 16, 2026

### Where the project stands

The web system is built and tested:
- **Students** request TOR and COE online.
- **Teachers** encode grades.
- **The registrar** approves and releases documents.
- **Every issued document** carries a document number and a QR code.
- **The scan station software** checks a printed document against the school's records and shows VALID, INVALID or NEEDS REVIEW.

Testing so far used sample layouts and fictional students. To finish on time, we need the items below. **Part A blocks our work now.** Part B is needed before we install the system.

Please write your answers under each item, or reply by email and quote the item number.

---

## Part A: Needed now (by October 9)

### A1. Your official document formats

Please send:

- [ ] **Transcript of Records (TOR):** the current official template (Word or PDF), and one or two filled examples with personal data removed or blacked out. Please include a TOR that runs to more than one page.
- [ ] **Certificate of Enrollment (COE):** the same: the template and one or two filled examples.
- [ ] **School logo** as an image file (PNG or SVG, as large as you have). The scan station uses it to check that a printed page carries the school's header.
- [ ] **Who signs each document**, with their exact name and title as printed, and whether the signature is wet-signed, printed, or both.

We will rebuild each format in the system, keeping your layout and wording. We will show you each one for approval before go-live.

### A2. Key decisions about scope

These decide what we deliver for this phase.

1. **Documents in this first release.** Is TOR + COE enough for now, with other documents (e.g. Certificate of Grades, Certificate of Registration, Diploma) in a later phase?

   _Answer:_

2. **Existing student system.** Do you already have a Student Information System or database? If yes: which product, who maintains it, and can we read data from it (exports, database access or an API)? Should the new system replace it, read from it, or run separately?

   _Answer:_

3. **What "verification" means for you.** The system confirms that a printed document's information **matches the school's official records** and that its document number was really issued. It does not examine signatures, dry seals or the paper itself. Is this acceptable for this phase?

   _Answer:_

4. **QR codes and document numbers on official documents.** May we print a QR code and a unique document number on every TOR and COE? (The QR code contains only a random code, never grades or personal data.) Would digital signatures be acceptable in a later phase?

   _Answer:_

5. **Legal standing.** Will scan results be used only internally by the registrar, or should they replace Certified True Copies? If the latter, has CHED or the relevant office been consulted?

   _Answer:_

6. **Output trays on the scan station.** We recommend two labelled trays (Single and Bulk) that the operator chooses before scanning. Is that acceptable, or do you need automatic sorting?

   _Answer:_

7. **Old records.** How many years of grades must be loaded before go-live, in what form (Excel, paper, old system), and who will prepare or clean them?

   _Answer:_

---

## Part B: Needed before installation (by October 12)

### B1. Where the system will run

The system will run on the web using three cloud services on their **free plans**:
- **Vercel:** the website.
- **Supabase:** the database and stored documents, in Singapore.
- **Render:** the application server, in Singapore.

8. **Accounts.** The accounts must belong to the school, not to us. Please give us a school Google account to sign up with, or create the three free accounts yourselves and invite our team.

   _Answer:_

9. **Web address.** Should the system use the free address the services provide (for example `adgvs.vercel.app`), or the school's own address (for example `records.yourschool.edu.ph`)? For your own address, your IT team needs to add one DNS record, which we will send.

   _Answer:_

10. **Backups.** The free database plan has no backups. We will run our own encrypted backup every night and keep 30 days. Who at the school will hold the backup password? It must be kept somewhere safe.

    _Answer:_

**What the free plans mean:**
- **Slow first page:** after about 15 minutes with no visitors, the first page can take up to a minute to open.
- **Storage:** there is 1 GB for stored documents and scan images, so old scan images will be deleted after a period you choose (question 28).
- **Commercial use:** the free website plan is meant for non-commercial use.

This setup is fine for the demo and the pilot. For full production use we recommend the paid plans, about US$45–50 a month in total.

### B2. Details printed on every document

Please give these exactly as they should appear:

| Item | Your answer |
| --- | --- |
| Full name of the institution | |
| Institution address | |
| Office name (e.g. "Office of the University Registrar") | |
| Registrar's name, as printed | |
| Registrar's title (e.g. "University Registrar") | |

### B3. How requests should work

11. **Fees.** Does the school charge for TOR or COE? If yes, the registrar will mark "payment confirmed" before a document is prepared. Online payment is not part of this phase.

    _Answer:_

12. **Release.** After the registrar approves a document, should the student be able to download it straight away, or only after collecting it at the office?

    _Answer:_

13. **Download period.** We assumed a student can download a released document for 30 days; the registrar can reopen it after that. Is 30 days right?

    _Answer:_

14. **Validity.** Should an issued document stop passing verification after a certain time (for example one year), or stay valid until revoked?

    _Answer:_

15. **Who prints the official copy:** the student at home, or the registrar on security paper?

    _Answer:_

16. **Approvers.** Is approval by the registrar alone enough, or must a dean or department head also approve?

    _Answer:_

17. **Who verifies documents:** registrar staff only, or will employers and other schools check documents directly in a later phase?

    _Answer:_

### B4. Grades

18. **Grading scale.** We assumed:
    - grades from 1.00 to 3.00 in steps of 0.25, plus 5.00 (failed), INC and DRP;
    - 3.00 is the passing grade;
    - the GWA includes every subject, including PE and NSTP.

    Please confirm or correct this, especially whether PE and NSTP count towards the GWA.

    _Answer:_

19. **When grades are final.** How do teachers submit grades today, and when are they considered final? In the system, teachers submit their grades and the registrar then locks the term. After that, any change needs the registrar's approval with a reason.

    _Answer:_

20. **Name format.** We print names as "MARIA R. SANTOS" (first name, middle initial, surname; suffix such as JR. at the end). Is that the format you use on TOR and COE?

    _Answer:_

### B5. Size of the school

21. How many students, teachers and registrar staff will use the system? About how many TOR/COE requests per month, normally and at peak?
22. How many scan stations are needed, where will they be placed, and how many documents a day will be checked (largest batch)?
23. One campus, or several?

_Answers:_

### B6. Logins and notifications

24. Should people sign in with their school Google or Microsoft account, or with the system's own email and password (the current setup)?
25. Are email or SMS notifications needed in this phase (for example "your document is ready")? They are not included at the moment.

_Answers:_

---

## Part C: Please confirm these working assumptions

We made these choices so work could continue. Tell us if any should change.

| # | What we did | OK? |
| --- | --- | --- |
| C1 | After 5 wrong passwords, an account is locked for 15 minutes, then unlocks by itself. The registrar or an administrator can unlock it sooner by resetting the password. | |
| C2 | The login page shows the same message for a wrong password and a locked account, so it never reveals whether an email address has an account. | |
| C3 | A student can cancel a request until the registrar approves it. Documents are prepared within seconds, so limiting cancellation to before preparation would leave no time at all. | |
| C4 | Registrar staff and system administrators can search the full activity log, including who changed what, before/after values, and the computer's network address. Students and teachers cannot see it. | |
| C5 | Only registrar staff given the "scan operator" permission can use the scan station and see scan results. | |

---

## Part D: For your Data Protection Officer

The system has security controls that support the school's compliance with the Data Privacy Act. Compliance itself remains the school's responsibility. Please pass these questions to your DPO; a short written answer or decision on each is enough. A detailed list of the personal data the system holds, who can see it, and how it moves is available on request.

26. Who is the school's Data Protection Officer? Are there existing privacy policies or a Privacy Impact Assessment we must follow?
27. **Privacy notice:** what should the portal tell users about what is collected, why, and for how long? Who writes and approves it?
28. **Retention:** how long should each of these be kept?
    - scan images;
    - verification results;
    - issued documents;
    - request records;
    - the activity log.
29. **Consent:** should students agree to third-party verification when they request a document?
30. **Breach response:** does the school's incident procedure cover this system, and who notifies the National Privacy Commission and affected students?
31. **Registration:** does this system need to be registered with the National Privacy Commission before go-live?
32. **Cloud hosting:** student records will be stored with Supabase and Render in Singapore, and the website served by Vercel. Are these providers and this location acceptable? The database is reachable over the internet, protected by strong passwords, a restricted application login and encrypted connections, rather than kept inside the school network. Is that acceptable?

_Answers:_

---

## Part E: Commercial

33. Is October 16 still the target, or is there a specific enrollment or graduation date the system must be ready for?
34. Who will own the source code and the scan station design after delivery? Is a maintenance and support contract expected after the warranty period?

_Answers:_

---

Thank you. Please send Part A as soon as you can, since the document formats are the main thing holding up the final layout and the scan checks. We're happy to go through any of these questions on a short call.
