""" member api endpoint """

import logging

from flask import current_app

from app.decorators import marshall_with
from app.models import MemberModel
from .api import api, members_request, members_response, members_create_request

logger = logging.getLogger(__name__)


def format_getmember(args):
    """ split query string on , to support GET multiple """
    return {key: args.get(key).split(',') for key, val in args.items()}


@api.route("/member", methods=["GET"])
@marshall_with(members_request, qs=True, formatter=format_getmember)
def get_member(params):
    """ get member object by id, phone, or mem_id """
    logger.info(f"parms {params}")

    id = params.get('id', [])
    phone = params.get('phone', [])
    mem_id = params.get('mem_id', [])

    if id:
        res = MemberModel(current_app).get("id", id)
    elif phone:
        res = MemberModel(current_app).get("phone", phone)
    elif mem_id:
        logger.info(f"type of mem id sent to GET model {type(mem_id[0])}")
        res = MemberModel(current_app).get("mem_id", mem_id)

    return {"members": members_response.dump(res)}, 200


@api.route("/member", methods=["POST"])
@marshall_with(members_create_request, qs=False)
def create_member(params):
    """ get member object by id, phone, or mem_id """
    logger.info(f"create member with {params}")

    res = MemberModel(current_app).create(params.get("members", []))

    return {"members": members_response.dump(res)}, 200
