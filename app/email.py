from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject, template, to, **shal):
    sender_email = 'shalin.rono@student.moringaschool.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + '.txt', **shal)
    email.html = render_template(template + '.html', **shal)
    mail.send(email)