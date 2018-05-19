FROM python:2.7
ADD . /WorkHub
WORKDIR /WorkHub
RUN pip install -r requirements.txt