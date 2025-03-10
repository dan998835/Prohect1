FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install vim -y
RUN apt-get install zip -y
RUN apt-get install unzip -y

COPY zip_job.py . /tmp/
RUN chmod +x /tmp/zip_job.py
WORKDIR /tmp
RUN uname -a
RUN test -f /tmp/zip_job.py && echo "file exists"
ENV VERSION=1.2.0
