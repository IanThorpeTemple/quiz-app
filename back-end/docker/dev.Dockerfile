FROM ubuntu:22.04

WORKDIR /code

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.server

EXPOSE 8000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]