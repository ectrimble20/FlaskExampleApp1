FROM python

MAINTAINER Eric Trimble "ectrimble84@gmail.com"

# copy data into app directory
COPY . /app

# run pip installation on requirements
RUN pip install -r /app/requirements.txt

# assign working directory to the www directory
WORKDIR /app/www

# Run the WSGI server
CMD ["python", "run.py"]

# exports the port we're running on
EXPOSE 5000