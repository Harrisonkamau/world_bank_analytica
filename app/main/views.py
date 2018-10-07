from flask_login import login_required
from flask import render_template
import requests

DATA_API_URL = 'http://api.worldbank.org/v2/datacatalog?format=json'

from . import main
from app.utils import filter_payload

@main.route('/')
@login_required
def index():
    data = requests.get(DATA_API_URL)
    filter_data = filter_payload(data.text)
    return render_template('base.html', data=filter_data)
