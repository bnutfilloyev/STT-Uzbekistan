FROM pytorch/pytorch:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y ffmpeg

RUN pip install -r requirements.txt && \
    pip install https://github.com/kpu/kenlm/archive/master.zip


