from flask import Blueprint
from flask import jsonify
from werkzeug import exceptions

errors = Blueprint('handlers', __name__)


class InvalidFileUpload(exceptions.HTTPException):
    # Default is bad request
    code = 400

    def __init__(self, message, status_code):
        exceptions.HTTPException.__init__(self)
        self.msg = message
        self.code = status_code


@errors.errorhandler(InvalidFileUpload)
def handle_invalid_filename(error):
    return jsonify({'message': error.msg, 'status_code': error.code})
