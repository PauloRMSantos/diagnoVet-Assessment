class TestStorage:
    def upload_pdf(self, file, filename: str) -> str:
        return f"gs://fake-bucket/{filename}"
