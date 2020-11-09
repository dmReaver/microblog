import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECREY_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # отключает функцию Flask-SQLAlchemy, которая мне 
                                            # не нужна, которая должна сигнализировать приложению 
                                            # каждый раз, когда в базе данных должно быть внесено 
                                            # изменение.

    