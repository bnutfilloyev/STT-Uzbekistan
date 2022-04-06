FROM huggingface/transformers-pytorch-gpu:latest

RUN apt update

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN cd bot

CMD ["python", "app.py"]