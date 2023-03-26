from flask import Flask
from . import (location, weather)

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(location.bp)
    app.register_blueprint(weather.bp)

    return app

