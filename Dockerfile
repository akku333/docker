FROM python:3

ADD encrypt.py /

RUN pip install pystrich
COPY encrypt.py ./encrypt.py

CMD [ "python", "./encrypt.py" ]
