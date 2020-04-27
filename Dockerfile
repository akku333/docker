FROM python:3

WORKDIR /user/src/app

ADD encrypt.py /

COPY . .

RUN pip install pystrich

RUN pip install pyAesCrypt

RUN python -m pip install --upgrade --user xmltodict

RUN [ "python", "./encrypt.py" ]
