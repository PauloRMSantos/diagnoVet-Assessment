from abc import ABC, abstractmethod

class FileStorage(ABC):
    @abstractmethod
    def upload_pdf(self, file, filename: str) -> str:
        pass