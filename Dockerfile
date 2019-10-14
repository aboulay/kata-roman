FROM ubuntu:18.04

RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.7

COPY ./translator /app/translator
COPY ./main.py /app/main.py

WORKDIR /app

CMD ["python3", "main.py", "16"]