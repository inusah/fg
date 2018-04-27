from flask import Flask
from flask_mail import Mail

from webceil.site import site
import config

mail = Mail()

app = Flask(__name__)

app.secret_key = config.SECRET_KEY

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = config.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = config.MAIL_PASSWORD

mail.init_app(app)

app.register_blueprint(site)
