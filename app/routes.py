from flask import Blueprint
import random, string

from . import db

from .models import User

letters = string.ascii_lowercase


app_routes = Blueprint('app_routes', __name__)
@app_routes.route('/')
def hello_world():
    user = ''.join(random.choice(letters) for i in range(8))
    mail = user + '@sap.com'
    user_record = User(username = user, email = mail)
    db.session.add(user_record)
    db.session.commit()

    return 'User = ' + user + ' ' + 'email' + mail