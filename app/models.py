from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, String, Text, Boolean
from database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(Text, nullable=False)

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.login)

    def generate_auth_token(self, expiration=3600):
        s = Serializer('SECRET_KEY', expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('SECRET_KEY')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(Text)
    finished = Column(Boolean)
    __table_args__ = (UniqueConstraint('user_id',
                                       'title',
                                       name='_user_task_uc'), )

    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.finished = False

    def __repr__(self):
        return '<task \'%r\'>' % (self.title)

    def to_JSON(self):
        return {
            "Id": self.id,
            "UserId": self.user_id,
            "Title": self.title,
            "Description": self.description,
            "IsFinished": self.finished
        }
