from flask import render_template

from . import site


@site.route('/')
def home():
    return render_template('site/index.html')


@site.route('/contact/')
def contact():
    return render_template('site/contact.html')


@site.route('/about/')
def about():
    return render_template('site/about.html')


@site.route('/portfolio/')
def portfolio():
    return render_template('site/portfolio.html')
