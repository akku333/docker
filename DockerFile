FROM python:3

ADD encrypt.py /

RUN pip install pystrich

CMD [ "python", "./encrypt.py" ]
