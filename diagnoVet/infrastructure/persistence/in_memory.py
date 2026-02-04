import uuid

class InMemoryReportRepository:
    def __init__(self):
        self.db = {}

    def save(self, data: dict, pdf_path: str) -> str:
        report_id = str(uuid.uuid4())
        self.db[report_id] = {
            "id": report_id,
            "data": data,
            "pdf_path": pdf_path
        }
        return report_id

    def get(self, report_id: str):
        return self.db.get(report_id)
