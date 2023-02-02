FROM python:3.7-alpine

COPY . /app
WORKDIR /app

EXPOSE 80

RUN pip install -r requirements.txt

CMD python -m nltk.downloader punkt; python server.py