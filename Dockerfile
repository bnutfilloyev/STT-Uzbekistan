FROM pytorch/pytorch:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y ffmpeg

RUN pip install -U --user pip numpy wheel packaging requests opt_einsum

RUN pip install -r requirements.txt && \
    pip install https://github.com/kpu/kenlm/archive/master.zip && \
    pip install transformers
    pip install pyctcdecod

