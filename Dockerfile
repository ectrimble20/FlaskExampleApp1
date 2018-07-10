FROM python

# copy files to src
COPY . /

WORKDIR /

# install python packages
RUN pip install -r /requirements.txt

RUN chmod +x /www/bin/run

# start WSGI server
CMD ["www/bin/run"]

# export port
EXPOSE 5000