# weather-app

## How to run this project you ask?

docker build -t weatherapp .
docker run -p 8080:8080 weatherapp

The app will be reachable on http://127.0.0.1:8080

or you can run it locally:

pip install -r requirements.txt
flask --app weatherapp run