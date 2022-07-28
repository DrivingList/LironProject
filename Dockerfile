FROM python:3.10

RUN pip install flask

WORKDIR /home/localadmin/ongoingProject/flaskexample
ADD app.py .
ENV FLASK_ENV=development

CMD python app.py
