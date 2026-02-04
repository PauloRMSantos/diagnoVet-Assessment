from application.interfaces.document_processor import DocumentProcessor

class TestDocumentProcessor(DocumentProcessor):
    def extract(self, content: bytes) -> dict:
        return {
            "patient": "Ramon",
            "owner": "João Silva",
            "veterinarian": "Dra. Ana",
            "diagnosis": "Normal",
            "recommendations": "Acompanhamento anual"
        }
