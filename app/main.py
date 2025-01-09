from fastapi import FastAPI
from app.views import router as views_router
from app.auth import router as auth_router

app = FastAPI()

# Rotas
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(views_router, prefix="/api", tags=["API"])

@app.get("/")
def home():
    return {"message": "Sistema de Reconhecimento de Objetos com FastAPI"}