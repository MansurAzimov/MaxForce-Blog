from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:user@localhost:5432/user'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)


from core import routes, models

