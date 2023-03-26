import requests

from flask import (Blueprint,render_template)
bp = Blueprint('weather', __name__, url_prefix='/weather')

base_url = 'https://api.open-meteo.com/v1/forecast'



def get_weather(latitude, longitude):
    query = f'?latitude={latitude}&longitude={longitude}&current_weather=true'
    try:
        response = requests.get(base_url+query)
        if response.status_code == 200:
            data = response.json()
            weather_code = data['current_weather']['weathercode']
            temperature = data['current_weather']['temperature']
            if weather_code <= 3:
                weather = 'Clear'
            else:
                weather = 'Cloudy'
            return render_template('weather.html', temperature=temperature, weather=weather)
        else:
            error = response.reason
            return render_template('error.html', error=error)
    except Exception as e:
        error = 'Weather Service unreachable'
        return render_template('error.html', error=error)
