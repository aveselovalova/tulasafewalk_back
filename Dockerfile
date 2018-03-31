FROM python:3

ADD model.py /
ADD server.py /

RUN pip install -r requierements.txt

CMD [ "python", "./server.py" ]
EXPOSE 5000