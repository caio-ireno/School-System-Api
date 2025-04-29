from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Config:
    HOST = '127.0.0.1'
    PORT = 5000
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Por padrão usa SQLite. Em produção, a variável DATABASE_URL do Render vai sobrescrever.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///school-db.db')
