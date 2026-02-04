from fastapi import APIRouter, UploadFile, File
from diagnoVet.application.use_cases.upload_report import UploadReportUseCase
from diagnoVet.infrastructure.persistence.firestore import ReportRepository

router = APIRouter(prefix="/api")

upload_use_case = UploadReportUseCase()
repo = ReportRepository()


@router.post("/report")
async def upload_report(file: UploadFile = File(...)):
    report_id = upload_use_case.execute(
        await file.read(),
        file.filename
    )
    return {"id": report_id}


@router.get("/report/{report_id}")
def get_report(report_id: str):
    return repo.get(report_id)
