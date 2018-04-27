from flask import render_template, request, flash
from flask_mail import Message, Mail
from .forms import ContactForm

from . import site


@site.route('/')
def home():
    return render_template('site/index.html')


@site.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(form.subject.data, sender='contact@webceil.com', recipients=['support@webceil.com'])
            mail = Mail()
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('site/contact.html', success=True, form=form)

    return render_template('site/contact.html', form=form)


@site.route('/about/')
def about():
    return render_template('site/about.html')


@site.route('/portfolio/')
def portfolio():
    return render_template('site/portfolio.html')
