from app import create_app, db, cli
from app.models import User, Post, Message, Notification, CalendarEvents

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification,
            'CalendarEvents' : CalendarEvents}


'''
pip freeze > requirements.txt
pip install -r requirements.txt

pip install:
- flask-wtf (для создания форм и их валидации)
- flask-sqlalchemy
- flask-migrate (миграции БД)
- flask-login (для поддержки регистрации)
- flask-mail (для поддержки эмейлов)
- pyjwt (для генерации токенов)
- flask-bootstrap (для красивых страниц)
- flask-moment (часы)
- flask-babel (перевод)
- langdetect (распознавание языка)
- requests
- python-dotenv
- elasticsearch
'''

'''
has_next: True, если после текущей есть хотя бы одна страница
has_prev: True, если есть еще одна страница перед текущей
next_num: номер страницы для следующей страницы
prev_num: номер страницы для предыдущей страницы
'''

'''
flask db init
flask db migrate -m "название файла"
flask db upgrade
flask db downgrade
'''
