FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

COPY . /app

RUN pip install --no-cache-dir -r backend/requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]