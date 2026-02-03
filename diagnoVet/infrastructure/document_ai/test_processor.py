from application.dtos import ExtractedReportData

class TestDocumentProcessor:
    def process(self, gcs_uri: str):
        return ExtractedReportData(
            patient="Paciente Teste",
            owner="Tutor Teste",
            veterinarian="Vet Teste",
            diagnosis="Diagnóstico Teste",
            recommendations="Recomendações Teste"
        )
