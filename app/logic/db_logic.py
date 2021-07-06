from database.database import db_session
from models import *
from security_logic import *


def add_task(user_id, title, description):
    new_task = Task(user_id, title, description)
    db_session.add(new_task)
    db_session.commit()
    return new_task.id


def add_user(login, password):
    registered_user = User(login, hashify_password(password))
    db_session.add(registered_user)
    db_session.commit()
    return registered_user.id


def is_users_task(user_id, id):
    return get_task_by_id(user_id, id) is not None


def get_task_by_id(user_id, id):
    task = Task.query.filter(Task.id == id).first()
    return task, task is None or task.user_id == user_id


def get_task_by_title(title, user_id):
    return Task.query.filter(Task.title == title).filter(
        Task.user_id == user_id).first()


def get_tasks_by_user_id(id):
    return [
        task for task in Task.query.filter(
            Task.user_id == id).order_by(Task.id).all()
    ]


def get_user_by_id(id):
    return User.query.filter(User.id == id).first()


def get_user_by_login(login):
    return User.query.filter(User.login == login).first()


def finish_task(task, finished):
    task.finished = finished
    db_session.commit()


def remove_task(user_id, task_id):
    task = get_task_by_id(user_id, task_id)
    if (task[0] is None or not task[1]):
        return
    db_session.delete(task[0])
    db_session.commit()


def update_task(user_id, task, title, description, finished):
    task.title = title
    task.description = description
    task.finished = finished
    db_session.commit()
