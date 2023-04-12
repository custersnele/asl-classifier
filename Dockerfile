FROM python:3.8-slim-buster

WORKDIR /app
RUN mkdir -p /uploads

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD resources resources
COPY app.py .

ENTRYPOINT ["python3", "app.py"]