from google.cloud import documentai
from google.api_core.client_options import ClientOptions


class DocumentAIProcessor:
    def __init__(self):
        self.project_id = "diagnovet-486321"
        self.location = "us"
        self.processor_id = "6221f9450c5388ca"

        opts = ClientOptions(
            api_endpoint=f"{self.location}-documentai.googleapis.com"
        )

        self.client = documentai.DocumentProcessorServiceClient(
            client_options=opts
        )

        self.name = self.client.processor_path(
            self.project_id,
            self.location,
            self.processor_id
        )

    def process(self, pdf_bytes: bytes):
        raw_document = documentai.RawDocument(
            content=pdf_bytes,
            mime_type="application/pdf"
        )

        request = documentai.ProcessRequest(
            name=self.name,
            raw_document=raw_document
        )

        result = self.client.process_document(request=request)
        return result.document
