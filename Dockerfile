FROM python:latest

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD python3 main.py
