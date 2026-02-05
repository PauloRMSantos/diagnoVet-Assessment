# diagnoVet – Veterinary Report Processing API

This project implements a backend API designed to ingest veterinary PDF reports, extract structured medical information, manage embedded image assets, and expose the processed data through a RESTful interface.

The solution is built with a strong focus on clean architecture, cloud-native design, and scalability, aligned with Google Cloud Platform services.

---

## Problem Statement

Veterinary diagnostic reports are commonly delivered as PDF documents containing both structured text and embedded images (e.g., radiographs).

The objective of this project is to:

1. Securely ingest PDF reports via an API  
2. Extract relevant medical and administrative information  
3. Extract and store embedded images as independent assets  
4. Persist structured metadata  
5. Expose all processed data through a retrieval API  

---

## Architecture Overview

The application follows Clean Architecture principles, ensuring separation of concerns and testability.

```
diagnoVet/
├── api/                    # HTTP layer (FastAPI routes)
├── application/            # Use cases / business logic
├── domain/                 # Core entities and interfaces
├── infrastructure/         # External services and adapters
└── main.py                 # Application entrypoint
```

### Architectural Principles

- Frameworks are treated as implementation details  
- Business logic is isolated from infrastructure  
- External services are accessed through abstractions  
- The system is designed to be cloud-agnostic where possible  

---

## Technology Stack

- Python 3  
- FastAPI – REST API framework  
- Google Cloud Document AI – OCR and structured document parsing  
- Google Cloud Storage – Image asset storage  
- PyMuPDF (fitz) – PDF image extraction  
- Uvicorn – ASGI server  

---

## Core Features

### 1. Secure PDF Ingestion

**Endpoint**

```
POST /reports
```

- Accepts PDF files using `multipart/form-data`
- Validates file type and size
- Initiates the document processing pipeline

---

### 2. Document Extraction Engine

Document parsing is implemented using Google Cloud Document AI (Custom Processor).

Extracted fields include:

- Patient  
- Owner  
- Veterinarian  
- Diagnosis  
- Recommendations  

The extraction logic is encapsulated in a dedicated infrastructure layer, allowing the processor to be replaced or extended without impacting the core application.

---

### 3. Image Asset Management

- Images are extracted from PDFs using PyMuPDF  
- Each image is uploaded to Google Cloud Storage  
- Images are referenced via public or signed URLs  

Example response fragment:

```json
{
  "images": [
    "https://storage.googleapis.com/diagnovet-reports-public/images/uuid.png"
  ]
}
```

---

### 4. Data Persistence and Retrieval

**Endpoint**

```
GET /reports/{id}
```

- Returns structured metadata extracted from the document  
- Includes associated image URLs  
- Designed to support Cloud Firestore or Cloud SQL  

---

## Local Development

```bash
pip install -r requirements.txt
uvicorn diagnoVet.main:app --reload
```

---

## Deployment Strategy

The application is designed to run on Google Cloud Run, using:

- Workload Identity (no service account keys)  
- Managed IAM permissions  
- Cloud Storage for image assets  
- Document AI for document processing  

### Deployment Note

A live deployment is intentionally omitted from this repository.

Document AI requires project-level IAM configuration, billing setup, and secure identity management. These requirements are outside the scope of this technical assessment, but the application is fully prepared for production deployment.

---

## Security Considerations

- No service account keys are stored in the repository  
- All cloud access relies on Application Default Credentials  
- Image access can be configured as:
  - Public (for demo purposes)
  - Signed URLs with expiration (production)

---

## Suggested Technical Walkthrough

A five-minute walkthrough would cover:

1. API usage via Postman or cURL  
2. PDF ingestion flow  
3. Image extraction and storage  
4. Document AI field extraction  
5. Architectural decisions and trade-offs  

---

## Future Improvements

- Asynchronous processing with Pub/Sub  
- Background jobs for large documents  
- Retry and dead-letter handling  
- Field confidence scoring  
- Frontend visualization of reports  

---

## Final Notes

This project demonstrates:

- Cloud-native backend architecture  
- Real-world document processing workflows  
- Clean Architecture applied in practice  
- Production-ready design decisions  

The codebase is intentionally structured to be maintainable, scalable, and extensible.
