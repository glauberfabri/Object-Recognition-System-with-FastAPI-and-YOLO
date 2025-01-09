import cv2
import torch
from app.models import SessionLocal, ImageAnalysis

# Carrega modelo YOLO
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

async def process_image(file):
    # Salva imagem localmente
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Carrega imagem
    img = cv2.imread(file_path)

    # Detecta objetos
    results = model(img)

    # Processa resultados
    detected_objects = results.pandas().xyxy[0]['name'].tolist()

    # Salva no banco
    session = SessionLocal()
    new_analysis = ImageAnalysis(image_name=file.filename, objects_detected=", ".join(detected_objects))
    session.add(new_analysis)
    session.commit()
    session.close()

    return {"image": file.filename, "objects_detected": detected_objects}
