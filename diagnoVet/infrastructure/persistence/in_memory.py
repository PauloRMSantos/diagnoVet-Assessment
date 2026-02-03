class InMemoryReportRepository:
    def __init__(self):
        self.db = {}

    def save(self, report):
        self.db[report.id] = report

    def get_by_id(self, report_id: str):
        return self.db.get(report_id)
