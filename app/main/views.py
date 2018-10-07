from flask_login import login_required
from flask import render_template
import requests
import ast

DATA_API_URL = 'http://api.worldbank.org/v2/datacatalog?format=json'

from . import main
from app.utils import metatype_filter, metatype_data

@main.route('/')
@login_required
def index():
    data = requests.get(DATA_API_URL).text
    metatype = metatype_data(data)
    filtered_data = metatype_filter(metatype)
    return render_template('base.html', data=filtered_data)
