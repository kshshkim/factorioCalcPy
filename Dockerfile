FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt-get update && apt-get upgrade -y
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
