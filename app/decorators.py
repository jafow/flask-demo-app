""" api decorators """
import logging

from functools import wraps
from flask import request
from marshmallow import ValidationError

logger = logging.getLogger()


def marshall_with(schema, formatter=None, qs=True):
    """
    validate and parse query params from url
    Args
        schema - marshmallow.Schema; schema to validate request data against
        formatter - [optional] function; formatter function passed request data before schema validation
        qs - bool; flag to indicate parsing urlencoded query strings or json from request body
    Returns:
        decorated function
    """

    def outer(fn):
        @wraps(fn)
        def inner():
            try:
                if qs:
                    args = request.args
                else:
                    args = request.get_json()

                if formatter is not None:
                    args = formatter(args)

                # validate request against schema
                logger.info(f"data {args}")

                parsed = schema.load(args)

                return fn(parsed)
            except (ValidationError, Exception) as err:
                logger.error("ValidationError %s", err)
                return {"status": "error", "msg": "Invalid Request"}, 400

        return inner

    return outer
