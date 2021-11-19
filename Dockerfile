FROM quay.io/bitnami/python:3.7-prod

EXPOSE 9010

ADD src /app

ENV FLASK_APP "app.py"

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
