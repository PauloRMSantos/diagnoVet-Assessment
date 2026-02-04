import os
from fastapi import FastAPI
from diagnoVet.api.routes import router

app = FastAPI(title="diagnoVet API")

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
