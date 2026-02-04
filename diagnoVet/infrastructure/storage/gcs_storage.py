from google.cloud import storage


class GCSStorage:
    def __init__(self):
        self.client = storage.Client()
        self.bucket_name = "diagnovet-reports-public"
        self.bucket = self.client.bucket(self.bucket_name)

    def upload_image(self, name: str, content: bytes) -> str:
        blob = self.bucket.blob(f"images/{name}")

        blob.upload_from_string(
            content,
            content_type="image/png"
        )

        # URL pública direta (bucket público)
        public_url = f"https://storage.googleapis.com/{self.bucket_name}/{blob.name}"

        return public_url
