FROM centos:centos8

RUN yum -y update; yum cleann all
RUN yum -y install epel-release; yum clean all
RUN yum -y install \
    python36 \
    python36-devel \
    which \
        ; yum clean all

RUN pip3 install --upgrade pip setuptools
RUN pip3 install pipenv

ENV LAN en_US.UTF-8

RUN mkdir -p /var/www/webapps
RUN mkdir /db

WORKDIR /var/www/webapps/requests

ADD Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system --dev

ADD . ./

RUN python3 manage.py migrate

EXPOSE 8080