"""DEV ONLY: run the API on a throwaway SQLite DB with demo data, on machines without
WeasyPrint (e.g. Windows). Never used in production; the app never imports this file.

    cd backend && .venv/Scripts/python scripts/dev_server.py

- Demo accounts use password "ChangeMe-2026" with the forced change switched off.
- PDF rendering returns the CI sample PDFs (scan-agent/tests/fixtures) instead of rendering.
- Maria's TOR from the CI sample is pre-issued, so scanning that PDF comes back VALID.
- Station "Dev Station" uses API key "dev-station-key".
"""

import json
import os
import sys
from datetime import timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT.parent / "scan-agent" / "tests" / "fixtures"
os.environ.setdefault("ADGVS_DATABASE_URL", f"sqlite:///{ROOT / 'dev.db'}")
os.environ.setdefault("ADGVS_STORAGE_DIR", str(ROOT / "storage-dev"))
os.environ.setdefault("ADGVS_COOKIE_SECURE", "false")
sys.path.insert(0, str(ROOT))

import uvicorn  # noqa: E402
from sqlalchemy import select  # noqa: E402

from app.db import Base, SessionLocal, engine  # noqa: E402
from app.documents import service  # noqa: E402
from app.documents.pdf import RenderedPdf  # noqa: E402
from app.main import app  # noqa: E402
from app.models import (  # noqa: E402
    DocumentRequest,
    DocumentTemplate,
    GeneratedDocument,
    ScanStation,
    Student,
    User,
)
from app.models.enums import (  # noqa: E402
    DocumentType,
    GeneratedDocumentStatus,
    RequestStatus,
    TemplateStatus,
)
from app.security import hash_token  # noqa: E402
from app.seed import seed  # noqa: E402
from app.timeutil import utcnow  # noqa: E402


def fake_render(html: str, footer_left: str, footer_right: str) -> RenderedPdf:
    name = "COE-2026-000001.pdf" if footer_left.startswith("COE") else "TOR-2026-000001.pdf"
    return RenderedPdf((FIXTURES / name).read_bytes(), page_count=1)


def prepare() -> None:
    Base.metadata.create_all(engine)
    with SessionLocal() as db:
        seed(db)
        for user in db.scalars(select(User)):
            user.must_change_password = False
        fixture = json.loads((FIXTURES / "TOR-2026-000001.json").read_text(encoding="utf-8"))
        number = fixture["snapshot"]["document_number"]
        existing = select(GeneratedDocument).where(GeneratedDocument.document_number == number)
        if db.scalar(existing) is None:
            maria = db.scalar(select(Student).where(Student.student_number == "2025-00001"))
            template = db.scalar(select(DocumentTemplate).where(
                DocumentTemplate.document_type == DocumentType.TOR,
                DocumentTemplate.status == TemplateStatus.ACTIVE))
            request = DocumentRequest(reference_no="REQ-DEV-000001", student_id=maria.id,
                                      document_type=DocumentType.TOR, purpose="Employment",
                                      status=RequestStatus.RELEASED)
            db.add(request)
            db.flush()
            db.add(GeneratedDocument(
                document_number=number, request_id=request.id, template_id=template.id,
                data_snapshot=fixture["snapshot"], data_hash=fixture["data_hash"],
                qr_token=fixture["qr_token"], page_count=1,
                status=GeneratedDocumentStatus.RELEASED, pdf_path=None,
                released_at=utcnow(), download_expires_at=utcnow() + timedelta(days=30)))
        if db.scalar(select(ScanStation).where(ScanStation.name == "Dev Station")) is None:
            db.add(ScanStation(name="Dev Station", api_key_hash=hash_token("dev-station-key")))
        db.commit()


if __name__ == "__main__":
    service.render_pdf = fake_render  # dev only: no WeasyPrint on this machine
    prepare()
    print("DEV server: demo password 'ChangeMe-2026'; station key 'dev-station-key'")
    uvicorn.run(app, host="127.0.0.1", port=8000)
