FROM python:3.6
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Shanghai
ADD . /srv/cookie_pool
WORKDIR /srv/cookie_pool
EXPOSE 5020

COPY ./sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev

RUN mv /bin/bash /bin/sh
RUN export LC_ALL=C
RUN source ~/.bashrc

RUN mkdir ~/.pip
COPY ./sources.list ~/.pip/pip.conf
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "run.py" ]