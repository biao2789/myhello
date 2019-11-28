from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask("sayhello")
app.config.from_pyfile("settings.py")

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# db.create_all()

from sayhello import forms, views
