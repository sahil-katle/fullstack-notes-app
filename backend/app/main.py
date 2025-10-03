from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.health import router as health_router

app = FastAPI(title="Notes API", version="0.1.0")

# CORS: allow the frontend (Vite) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount routers (keeps endpoints organized)
app.include_router(health_router, prefix="/health", tags=["health"])
