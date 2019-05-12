FROM python:3.7

RUN pip3 install pipenv

RUN mkdir -p keyauth

COPY . keyauth

RUN chmod 755 keyauth

WORKDIR keyauth

RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000

CMD flask run --host=0.0.0.0
