FROM debian:latest

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv venv

RUN /app/venv/bin/pip install -r requirements.txt

CMD ["/app/venv/bin/python", "main.py"]