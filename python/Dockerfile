FROM python:3.7.6-slim-stretch
RUN pip install gunicorn==20.0.4
ADD server.py .
CMD ["gunicorn", "-b", ":5000", "--statsd-host", "statsd:8125", "server:app"]
