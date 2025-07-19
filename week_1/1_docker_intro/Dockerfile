FROM python:3.12.8

RUN pip install pandas

WORKDIR /app
COPY docker_test.py docker_test.py

ENTRYPOINT ["python", "docker_test.py"]