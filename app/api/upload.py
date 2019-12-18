import logging

from flask import request
from .api import upload

from app.worker import tasks


logger = logging.getLogger(__name__)


@upload.route("/upload", methods=["POST"])
def post_member():
    """
    Client chunks the file upload and sends a payload of (uuid, buffer).
    API quickly funnels each chunk onto the upload_chunk task for deduping
    and storing and returns 100 continue to the client.
    """
    (guid, chunk) = request.get_data()
    tasks.upload_chunk.apply_async(args=[guid, chunk], countdown=4)

    return {"status": "ok", "msg": "posted ok"}, 100
