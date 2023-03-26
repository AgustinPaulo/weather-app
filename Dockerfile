FROM python:3.9-alpine

WORKDIR /weatherapp
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["flask", "--app", "weatherapp", "run", "--host=0.0.0.0", "--port=8080"]