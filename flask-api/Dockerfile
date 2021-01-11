FROM debian:stable

RUN apt-get update && apt-get install python3-pip python3-dev default-libmysqlclient-dev curl -y

ADD ./project /code
WORKDIR /code

RUN echo $(ls /code)
RUN pip3 install -r /code/requirements.txt

#ENTRYPOINT tail -f /dev/null
#ENTRYPOINT python3 main.py
ENTRYPOINT gunicorn -c gunicorn.py main:app
