FROM python

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /src
WORKDIR /src
CMD gunicorn --bind 0.0.0.0:5000 --workers 10 example:app
EXPOSE 5000