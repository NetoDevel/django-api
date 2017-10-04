FROM nginx

RUN apt-get update -qq && apt-get -y install apache2-utils

ENV NGINX_ROOT /server

RUN mkdir -p $NGINX_ROOT

WORKDIR $NGINX_ROOT

RUN mkdir log

COPY nginx.conf /etc/nginx/

CMD [ "nginx", "-g", "daemon off;" ]
