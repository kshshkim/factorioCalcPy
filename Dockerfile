FROM tiangolo/uwsgi-nginx-flask
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY . /FactorioCalcBase
COPY . /FactorioCalcWeb