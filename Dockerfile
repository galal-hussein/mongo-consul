FROM ubuntu:latest
MAINTAINER Hussien Galal
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

RUN apt-get update -q
RUN apt-get install -yqq python python-dev python-pip mongodb-org

RUN mkdir -p /data/db
RUN mkdir -p /var/register
WORKDIR /var/register

ADD scripts/requirements.txt /var/register/
ADD scripts/register.py /var/register/
ADD scripts/run.sh /var/register/

RUN chmod u+x register.py
RUN chmod u+x run.sh
RUN pip install -r requirements.txt

EXPOSE 27017 28017
ENTRYPOINT ["/var/register/run.sh"]
CMD []
