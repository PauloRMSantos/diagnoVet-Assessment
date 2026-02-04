from google.cloud import firestore


class ReportRepository:
    def __init__(self):
        self.db = firestore.Client()
        self.collection = self.db.collection("reports")

    def save(self, data: dict):
        doc_ref = self.collection.document()
        doc_ref.set(data)
        return doc_ref.id

    def get(self, report_id: str):
        doc = self.collection.document(report_id).get()
        return doc.to_dict()
