from fastapi import APIRouter, UploadFile, HTTPException
from app.controllers import process_image

router = APIRouter()

@router.post("/upload/")
async def upload_image(file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Formato de imagem inválido")
    
    result = await process_image(file)
    return result
