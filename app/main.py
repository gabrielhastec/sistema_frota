
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import motoristas, veiculos, viagens

app = FastAPI(title="Sistema de Frota", version="1.0.0")

# CORS para frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(motoristas.router, prefix="/api/v1")
app.include_router(veiculos.router, prefix="/api/v1")
app.include_router(viagens.router, prefix="/api/v1")