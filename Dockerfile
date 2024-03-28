FROM python:3

WORKDIR /tracker

COPY ./requirements.txt /tracker/

RUN pip3 install -r /tracker/requirements.txt

COPY . .
