from app.celery import queue


@queue.task
def upload_chunk(chunkid, buf):
    a = {
        "key": "val",
        "x": [1, 2, 3, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3],
    }
    return a
