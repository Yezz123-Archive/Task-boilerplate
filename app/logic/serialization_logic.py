from flask import json


def serialize_single_task(task):
    return json.dumps(task.to_JSON())


def serialize_tasks(tasks):
    return '[{0}]'.format(','.join(
        [serialize_single_task(task) for task in tasks]))


def serialize_task_list(tasks):
    return serialize_tasks(tasks)


def serialize_user_info(user):
    if user == None:
        return json.dumps({"login": "None", "IsAuthenticated": False})
    else:
        return json.dumps({"login": user.login, "IsAuthenticated": True})