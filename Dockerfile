FROM python:3.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN python -m spacy download de_dep_news_trf

COPY . .

ENTRYPOINT [ "python", "spert.py", "api", "--config", "configs/financial_statements_predict.conf" ]