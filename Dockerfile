FROM python:3.6.4-alpine3.7
RUN set -xe \
	&& pip install requests \
	&& mkdir -p /app
COPY weather.py /app/
WORKDIR /app
CMD ["python","weather.py"]
