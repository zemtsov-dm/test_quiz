FROM tiangolo/uvicorn-gunicorn:python3.11-slim
RUN apt-get update && apt-get install wget gcc -y
RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
