class ImageAsset:
    def __init__(self, url: str):
        self.url = url


class MedicalReport:
    def __init__(
        self,
        id: str,
        patient: str,
        owner: str,
        veterinarian: str,
        diagnosis: str,
        recommendations: str
    ):
        self.id = id
        self.patient = patient
        self.owner = owner
        self.veterinarian = veterinarian
        self.diagnosis = diagnosis
        self.recommendations = recommendations
        self.images: list[ImageAsset] = []

    def add_image(self, image: ImageAsset):
        self.images.append(image)