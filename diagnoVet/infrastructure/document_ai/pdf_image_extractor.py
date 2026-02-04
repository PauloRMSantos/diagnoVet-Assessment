import fitz  # PyMuPDF
import uuid


class PDFImageExtractor:
    def extract(self, pdf_bytes: bytes):
        images = []
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        for page in doc:
            for img in page.get_images(full=True):
                xref = img[0]
                base_image = doc.extract_image(xref)
                images.append({
                    "name": f"{uuid.uuid4()}.png",
                    "bytes": base_image["image"]
                })

        return images
