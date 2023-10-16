# Imagem base
FROM python:3.10.2-slim

ENV TZ=America/Sao_Paulo
ENV LANG C.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL C.UTF-8

RUN apt update && apt install -y

WORKDIR /home/app/
COPY . /home/app/
COPY requirements.txt /home/app
RUN pip install -r requirements.txt

CMD [ "tail", "-f", "/dev/null" ]
