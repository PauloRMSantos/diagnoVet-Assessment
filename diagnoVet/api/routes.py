from fastapi import APIRouter, File, UploadFile

from application.use_cases.upload_report import UploadReportUseCase
from infrastructure.document_ai.test_processor import TestDocumentProcessor
from infrastructure.persistence.in_memory import InMemoryReportRepository
from infrastructure.storage.test_storage import TestStorage


router = APIRouter()

use_case = UploadReportUseCase(
    storage = TestStorage(),
    processor = TestDocumentProcessor(),
    repository = InMemoryReportRepository()
)

@router.post("/report")
async def upload_report(file: UploadFile = File(...)):
    report_id = use_case.execute(file.file)
    return {"report_id": report_id}