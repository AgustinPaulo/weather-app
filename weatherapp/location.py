from flask import (Blueprint, request, render_template)
from . import weather as ws
bp = Blueprint('location', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def location():
    if request.method == 'POST':
        latitude = request.form.get("latitude")
        longitude = request.form.get("long")
        if not latitude or not longitude:
            error = 'One of the location parameters is missing'
            render_template('error.html', error=error)
        return ws.get_weather(latitude=latitude, longitude=longitude)

    return render_template('location.html')