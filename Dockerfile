FROM pytorch/pytorch:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y ffmpeg && \
    apt-get -y install build-essential libboost-all-dev cmake zlib1g-dev libbz2-dev liblzma-dev

RUN apt-get install -y libboost-all-dev libeigen3-dev

RUN pip install -U pip numpy wheel packaging requests opt_einsum

RUN pip install -r requirements.txt && \
    pip install https://github.com/kpu/kenlm/archive/master.zip && \
    pip install transformers && \
    pip install pyctcdecod

