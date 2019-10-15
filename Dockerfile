FROM ubuntu:18.04

RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.7

COPY ./translator /app/translator
COPY ./main.py /app/main.py

WORKDIR /app

ENTRYPOINT [ "python3 main.py" ]