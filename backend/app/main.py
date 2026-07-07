from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ask import router as ask_router
from app.api.upload import router as upload_router


app = FastAPI(
    title="AI Business Analytics Assistant",
    description="AI-powered dataset analysis and business insights API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)
app.include_router(ask_router)


@app.get("/")
def root():
    return {
        "message": "AI Business Analytics Assistant API is running"
    }