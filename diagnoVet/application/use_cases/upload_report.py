import uuid

from domain.Entities import MedicalReport


class UploadReportUseCase:

    def __init__(self, storage, processor, repository):
        self.storage = storage
        self.processor = processor
        self.repository = repository

    def execute(self, pdf_file):
        report_id = str(uuid.uuid4())

        pdf_uri = self.storage.upload_pdf(
            pdf_file,
            f"{report_id}.pdf"
        )

        data = self.processor.process(pdf_uri)

        report = MedicalReport(
            report_id,
            data.patient,
            data.owner,
            data.veterinarian,
            data.diagnosis,
            data.recommendations
        )

        self.repository.save(report)
        return report_id
