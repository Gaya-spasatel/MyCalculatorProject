FROM python:3.10


COPY calculatorService/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./calculatorModule /calculatorModule
WORKDIR /calculatorModule
RUN pip install .

COPY  calculatorService/calculatorAPI /app/calculatorAPI
COPY calculatorService/calculatorService /app/calculatorService
COPY calculatorService/manage.py /app/manage.py
COPY calculatorService/app_uwsgi.ini /app/app_uwsgi.ini
WORKDIR /app

RUN python manage.py migrate
ENTRYPOINT [ "uwsgi", "app_uwsgi.ini" ]