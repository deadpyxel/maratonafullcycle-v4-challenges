FROM python:3-slim-buster
ENV PYTHONUNBUFFERED 1
# Application destination
RUN mkdir /code
WORKDIR /code
# Setup dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Copy application
COPY . /code/
EXPOSE 8080

CMD ["python", "server.py"]
