from flask import Flask

from bcomtech.site import site

app = Flask(__name__)

app.register_blueprint(site)
