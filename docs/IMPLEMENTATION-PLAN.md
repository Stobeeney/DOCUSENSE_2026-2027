# Implementation Plan (2-week build)

Source of truth for scope: [MVP-Specification.md](MVP-Specification.md).
Tracking: Proyekto project "Academic Document Generation Validation System" (roadmap with 9 epics, 4 milestones).

## Team

| Member | Area | Owns |
| --- | --- | --- |
| JC (Juan Carlos Gan) | Software | Backend API, web app, document generation, OCR/validation engine, deployment |
| Daniel (Daniel Rein Cosare) | Hardware | Scanner + mini PC procurement, station setup, scanner capture in the scan agent, enclosure/trays, OCR test runs |

## Timeline

The spec estimates 16–18 weeks for 3 people. This plan compresses it to **Oct 5–16, 2026** by running tracks in parallel, using AI-assisted development, and building validation against file-drop images before the scanner arrives. The compression only holds if client inputs (templates, Section 28 Q1–7) arrive by **Oct 6** and hardware is on hand by **Oct 7**.

| Dates | Software (JC) | Hardware (Daniel) |
| --- | --- | --- |
| Oct 5–7 | Repo, Docker, schema, auth/RBAC, audit | Order scanner + mini PC, verify driver |
| Oct 6–8 | Academic records, grades, locking | Station OS setup, enclosure design (1 review round) |
| Oct 7–9 | Templates + PDF generation (doc no., QR, snapshot, hash) | Scanner capture module |
| Oct 8–13 | OCR + validation engine (file-drop first) | Single/bulk sessions, page splitting, jam handling |
| Oct 9–12 | Requests + approval workflow | Fabricate enclosure |
| Oct 12–14 | Dashboards | Optional diverter/light |
| Oct 13–16 | Tests, deploy, manuals, demo | OCR accuracy run, tamper tests, station install |

Milestones: **M1** records working (Oct 8) · **M2** documents generated & released (Oct 12) · **M3** scan-to-result (Oct 14) · **M4** demo / go-live (Oct 16).

## Repository layout

```
backend/      FastAPI + SQLAlchemy + Alembic (API, generation, validation rules)
frontend/     React (Vite) + Tailwind dashboards
scan-agent/   Python station agent (capture, clean-up, QR, OCR, upload)
docs/         Spec, plan, guides
```

## Technical decisions

- **Postgres in production, SQLite for tests.** JSON columns use `JSON().with_variant(JSONB, "postgresql")`, so tests run without a database server.
- **Server-side sessions** (`user_sessions` table) instead of JWT. That gives real logout, the 30-minute idle timeout and lockout without token revocation lists.
- **`scan_stations` table** for per-station API keys (Section 18). With `user_sessions` this makes 19 tables instead of the spec's 17.
- **Validation rules live in the backend** (pure functions, unit-tested). The scan agent only extracts fields and confidences.
- **File-drop mode** in the scan agent is built first, so OCR work does not wait on hardware.

## Open items blocking the critical path

1. Official TOR/COE templates + anonymized samples (Section 28 Q14).
2. Written answers to Section 28 Q1–7.
3. Scanner model with confirmed TWAIN/SANE driver.
4. Hosting decision (on-prem vs cloud), Q12.
