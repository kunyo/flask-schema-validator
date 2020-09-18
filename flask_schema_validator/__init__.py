import json
import sys
import jsonschema
from flask import request
from functools import wraps

def validate(f=None, schema:dict=None):
    if f is not None and schema is not None:  # pragma: no cover
        raise ValueError(
            'data and schema are the only supported arguments')

    def validate_internal(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if request.method != 'OPTIONS':  # pragma: no cover
                if not request.is_json:
                    return 'Invalid request', 400

                request_struct = None
                try:
                    request_struct = json.loads(request.json)
                except:
                    return 'Cannot parse request body', 400

                try:
                    jsonschema.validate(instance=request_struct, schema=schema)
                except jsonschema.exceptions.ValidationError as err:
                    return 'Schema validation failed: %s' % err.message, 400

                request.json_instance = request_struct
            return f(*args, **kwargs)
        return decorated

    return validate_internal