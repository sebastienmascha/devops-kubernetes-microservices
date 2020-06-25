FROM python:3.7
RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /tmp/myapp
RUN pip install /tmp/myapp
WORKDIR /tmp/myapp

ENV FLASK_ENV="development"

RUN python3 -m textblob.download_corpora

ENTRYPOINT ["python3"]
CMD ["/tmp/myapp/sentiment_analysis.py"]
