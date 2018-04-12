from flask import Flask

from webceil.site import site

app = Flask(__name__)

app.register_blueprint(site)
