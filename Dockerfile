FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt-get update && apt-get upgrade -y
COPY . /app
