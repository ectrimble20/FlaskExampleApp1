FROM python

# copy files to src
COPY . /app

WORKDIR /app

# install python packages
RUN pip install -r /app/requirements.txt

# start WSGI server
CMD ["python", "www/example.py"]

# export port
EXPOSE 5000