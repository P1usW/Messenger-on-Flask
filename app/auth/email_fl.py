from flask_mail import Message
from app import mail, celery
from flask import render_template, current_app


@celery.task(name='app.auth.send_password_reset_email')
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    app = current_app._get_current_object()

    subject = '[Microblog] Reset Your Password'
    sender = current_app.config['ADMINS'][0]
    recipients = [user.email]
    text_body = render_template('email/reset_password.txt', user=user, token=token)
    html_body = render_template('email/reset_password.html', user=user, token=token)

    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    mail.send(msg)

#current_app — это переменная контекста, привязанная к потоку, который обрабатывает клиентский запрос
#current_app на самом деле является proxy object, который динамически сопоставляется с экземпляром приложения.
#Выражение current_app._get_current_object() извлекает фактический экземпляр приложения из объекта прокси,
#так что это то, что я передал потоку в качестве аргумента.