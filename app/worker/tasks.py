from app.celery import queue


@queue.task
def add(req_val: str):
    print("adding x y", req_val)
    return f"{req_val} -- buttttt"
