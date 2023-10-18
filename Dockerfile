FROM python:3.8-slim-buster

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

COPY ./ /app

WORKDIR /app


CMD ["/app/entrypoint.sh"]