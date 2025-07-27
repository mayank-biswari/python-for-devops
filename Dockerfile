FROM python:3.9-alpine

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

COPY . /app

EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]