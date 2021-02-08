from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import random, string
letters = string.ascii_lowercase


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    user = ''.join(random.choice(letters) for i in range(8))
    mail = user + '@sap.com'
    user_record = User(username = user, email = mail)
    db.session.add(user_record)
    db.session.commit()

    return 'User = ' + user + ' ' + 'email' + mail


if __name__ =='__main__':
    app.run(debug=True)