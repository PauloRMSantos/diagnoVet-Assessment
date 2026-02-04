class DocumentAIFieldParser:
    def parse(self, document):
        data = {}

        for entity in document.entities:
            field_name = entity.type_.lower()
            data[field_name] = entity.mention_text

        return {
            "patient": data.get("patient"),
            "owner": data.get("owner"),
            "veterinarian": data.get("veterinarian"),
            "diagnosis": data.get("diagnosis"),
            "recommendations": data.get("recommendations"),
        }
