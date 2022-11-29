FROM python:3.6.1-alpine
RUN pip install --upgrade pip
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code
CMD ["python", "app.py"]