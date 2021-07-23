FROM tiangolo/uwsgi-nginx-flask
#COPY requirements.txt /tmp/
RUN apt-get update && apt-get upgrade -y
RUN pip install -U pip
RUN echo -e "\nenable-threads = true" >> /app/uwsgi.ini

#RUN pip install -r /tmp/requirements.txt
COPY . /app
