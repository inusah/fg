from flask import render_template

from . import site


@site.route('/')
def home():
    return render_template('site/index.html')
