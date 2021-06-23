FROM python:3.8-slim

WORKDIR /app/
ADD ./requirements.txt /app/requirements.txt

RUN apt-get update

RUN pip3 install -r requirements.txt

COPY ./ /app/
WORKDIR /app/

ENTRYPOINT ["python", "run.py"]
