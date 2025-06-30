FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    build-essential \
    python3.10 \
    python3-pip \
    python3.10-venv \
    uvicorn \
    tesseract-ocr \
    tesseract-ocr-por \
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./ /app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["fastapi", "run"]
