from app.celery import queue


@queue.task
def upload_chunk(chunkid, buf):
    pass
