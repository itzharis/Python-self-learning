FROM ubuntu:latest

RUN apt update
Run apt install python3 -y

WORKDIR /var/www/html
COPY print.py ./
CMD [ "python3", "./print.py"]

