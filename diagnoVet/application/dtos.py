from pydantic import BaseModel

class ExtractedReportData(BaseModel):
    patient: str
    owner: str
    veterinarian: str
    diagnosis: str
    recommendations: str
