FROM python:3.7

ENV SRC /home/www/dockerdemo2

RUN mkdir -p /home/www/dockerdemo2

WORKDIR $SRC
RUN rm -rf $SRC
COPY . $SRC

RUN pip3 install -r $SRC/requirements.txt
# CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8080"]
RUN chmod 777 run.sh
#CMD ./run.sh
CMD /bin/bash run.sh