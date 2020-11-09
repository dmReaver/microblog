import os


class Config:
    SECRET_KEY = os.environ.get('SECREY_KEY') or 'you-will-never-guess'
    