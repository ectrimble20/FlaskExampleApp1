FROM python

MAINTAINER Eric Trimble "ectrimble84@gmail.com"

# copy pip file
COPY requirements.txt /requirements.txt

# run pip installation on requirements
RUN pip install -r /requirements.txt

# copy everyting into app directory
COPY . /app

# assign working directory to the www directory
WORKDIR /app/www

# exports the port we're running on
EXPOSE 5000

# execution command for the shell wrapper
CMD ["bin/run"]
