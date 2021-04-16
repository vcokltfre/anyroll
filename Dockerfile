FROM python:3.8

WORKDIR /app

RUN pip install fastapi uvicorn

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
