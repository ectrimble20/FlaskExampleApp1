FROM python

MAINTAINER Eric Trimble "ectrimble84@gmail.com"

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY /www /www
WORKDIR /src

EXPOSE 5000

CMD ["bin/run"]
