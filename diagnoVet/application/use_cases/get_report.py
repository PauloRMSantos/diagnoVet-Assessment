class GetReportUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, report_id: str):
        report = self.repository.get(report_id)
        if not report:
            raise ValueError("Report not found")
        return report
