FROM python:3.6

RUN pip install flask

COPY . /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
