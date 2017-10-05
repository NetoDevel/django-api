FROM python:2.7-onbuild

RUN \
    apt-get update &&\
    apt-get -y install \
        libpq-dev \
        python-dev

ENV APP_ROOT .

RUN mkdir -p $APP_ROOT

WORKDIR $APP_ROOT

RUN pip install -r requirements.txt

COPY . $APP_ROOT

EXPOSE 8000
