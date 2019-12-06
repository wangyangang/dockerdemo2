FROM python:3.7
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
COPY pip.conf /root/.pip/pip.conf
RUN pip install -r /usr/src/app/requirements.txt
RUN rm -rf /usr/src/app

COPY . /usr/src/app
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8080"]
