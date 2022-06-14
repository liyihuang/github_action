FROM python:3.9.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/hello.py .

EXPOSE 8080

CMD [ "python", "./hello.py" ]