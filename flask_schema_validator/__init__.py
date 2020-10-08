import json
import sys
import jsonschema
from flask import request
from functools import wraps


def validate(f=None, schema: dict = None):
  if f is not None and schema is not None:  # pragma: no cover
    raise ValueError(
        'data and schema are the only supported arguments')

  def validate_internal(f):
    @wraps(f)
    def decorated(*args, **kwargs):
      if request.method != 'OPTIONS':  # pragma: no cover
        if not request.is_json:
          return 'Invalid request', 400

        try:
          jsonschema.validate(instance=request.json, schema=schema)
        except jsonschema.exceptions.ValidationError as err:
          return 'Schema validation failed: %s' % err.message, 400
      return f(*args, **kwargs)
    return decorated

  return validate_internal
