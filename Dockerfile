FROM python:3.9.2

ENV TZ=Europe/Vienna
WORKDIR /usr/src/pyapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY .env .

CMD [ "python3", "main.py" ]
