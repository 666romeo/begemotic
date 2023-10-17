FROM python:3.8

WORKDIR /app

COPY ./app /app
COPY requirements.txt /app

RUN chmod +x startup.sh
RUN pip install -r requirements.txt

EXPOSE 8000
