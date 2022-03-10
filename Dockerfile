FROM huggingface/transformers-pytorch-gpu:latest

RUN apt update

WORKDIR /app

COPY . .

RUN cd Training

CMD ["/usr/bin/bash", "run.sh"]

