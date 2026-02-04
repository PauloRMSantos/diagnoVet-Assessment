import os
import uuid


class LocalStorage:
    def __init__(self, base_path="data"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)
        
    def upload(self, path: str, content: bytes) -> str:
        filename = f"{uuid.uuid4()}_{path}"
        full_path = os.path.join(self.base_path, filename)

        with open(full_path, "wb") as f:
            f.write(content)
        
        return full_path