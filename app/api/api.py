from flask import Blueprint
import marshmallow

from app.extensions import ma

api = Blueprint("member", "member")
upload = Blueprint("upload", "upload")


# Response schema
class MemberSchema(ma.Schema):
    """ member API response schema """

    class Meta:
        # expose only these fields in response
        fields = ("id", "mem_id", "fname", "lname", "acct_id")


# Request schema
class MemberRequestSchema(marshmallow.Schema):
    id = marshmallow.fields.List(marshmallow.fields.Str(), required=False)
    phone = marshmallow.fields.List(marshmallow.fields.Str(required=False))
    mem_id = marshmallow.fields.List(marshmallow.fields.Int(required=False))


class MemberCreateSchema(marshmallow.Schema):
    """ create schema single member """

    fname = marshmallow.fields.Str(required=False)
    lname = marshmallow.fields.Str(required=False)
    phone = marshmallow.fields.Str(required=True)
    mem_id = marshmallow.fields.Int(required=True)


class MemberCreateList(marshmallow.Schema):
    """ nested schema create members """

    members = marshmallow.fields.List(marshmallow.fields.Nested(MemberCreateSchema))


members_response = MemberSchema(many=True)
members_request = MemberRequestSchema()
members_create_request = MemberCreateList()
