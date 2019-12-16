
from flask import Blueprint, request

from app.worker import tasks

upload = Blueprint('upload', __name__)


@upload.route("/butt/<taskid>", methods=["GET"])
def get_butt(taskid):
    task_result = tasks.add.AsyncResult(taskid)
    if task_result.state == "PENDING":
        return {
            "status": "ok",
            "msg": "pending"
        }, 202
    elif task_result.state != "FAILURE":
        xx = task_result.result
        return {
            "status": "ok",
            "msg": xx
        }, 200

    return {"status": "err", "msg": "fail"}, 400


@upload.route("/butt", methods=["POST"])
def post_butt():
    body = request.get_json()
    name = body.get("name")
    print("posted name::: ", name)

    t = tasks.add.apply_async(args=[name], countdown=4)
    return {"status": "ok", "msg": "posted ok", "taskid": t.id}, 202
