FROM nginx:latest

RUN apt-get update && apt-get install curl -y

RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime

ENTRYPOINT nginx -g 'daemon off;'
