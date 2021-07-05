from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

app = Flask(__name__)

# Replace [PASSWORD] with the root password for your mysql container
password = os.getenv('password')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{password}@mysql:3306/flaskdb"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email, ' Name: ', self.first_name, ' ', self.last_name, '\n'])


@app.route('/')
def hello():
    data1 = Users.query.all()
    return render_template('home.html', data1=data1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
