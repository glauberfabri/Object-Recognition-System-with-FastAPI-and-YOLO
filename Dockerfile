FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Executar testes antes de iniciar a aplicação
RUN pytest --disable-warnings

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
