from abc import ABC, abstractmethod

class ReportRepository(ABC):
    @abstractmethod
    def save(self, data: dict, pdf_path: str) -> str:
        pass

    @abstractmethod
    def get(self, report_id: str) -> dict:
        pass
