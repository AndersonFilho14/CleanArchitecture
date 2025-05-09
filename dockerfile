# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install uv
COPY . .
RUN uv sync
RUN apt-get update && \
    apt-get install -y \
    git \
    unixodbc \
    unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*


CMD ["uv", "run", "run.py"]
