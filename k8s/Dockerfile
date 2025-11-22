FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

COPY env/ ./env 

# Default environment (can be overridden at runtime)
ENV ENV=dev

EXPOSE 80

CMD ["uvicorn","app.main.app","--host","--port","80"]