FROM python:3

ADD model.py /
ADD server.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./server.py" ]
EXPOSE 5000