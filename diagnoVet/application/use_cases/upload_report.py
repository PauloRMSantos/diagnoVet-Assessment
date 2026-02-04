from diagnoVet.infrastructure.document_ai.document_processor import DocumentAIProcessor
from diagnoVet.infrastructure.document_ai.field_parser import DocumentAIFieldParser
from diagnoVet.infrastructure.document_ai.pdf_image_extractor import PDFImageExtractor
from diagnoVet.infrastructure.storage.gcs_storage import GCSStorage
from diagnoVet.infrastructure.persistence.firestore import ReportRepository


class UploadReportUseCase:
    def __init__(self):
        self.processor = DocumentAIProcessor()
        self.parser = DocumentAIFieldParser()
        self.image_extractor = PDFImageExtractor()
        self.storage = GCSStorage()
        self.repo = ReportRepository()

    def execute(self, pdf_bytes: bytes, filename: str):
        document = self.processor.process(pdf_bytes)
        fields = self.parser.parse(document)

        images = self.image_extractor.extract(pdf_bytes)
        image_urls = [
            self.storage.upload_image(img["name"], img["bytes"])
            for img in images
        ]

        report = {
            "filename": filename,
            "fields": fields,
            "images": image_urls
        }

        report_id = self.repo.save(report)
        return report_id
