FROM pytorch/pytorch:latest


WORKDIR /app

RUN apt update

COPY . .

RUN pip install -r requirements.txt

RUN cd bot

CMD ["python", "app.py"]