FROM tutum/mongodb
MAINTAINER Hussien Galal
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -q
RUN apt-get install -yqq python python-dev python-pip

RUN mkdir -p /var/register
WORKDIR /var/register

ADD scripts/requirements.txt /var/register/
ADD scripts/register.py /var/register/
ADD scripts/run.sh /var/register/

RUN chmod u+x register.py
RUN chmod u+x run.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["/var/register/run.sh"]
CMD []
