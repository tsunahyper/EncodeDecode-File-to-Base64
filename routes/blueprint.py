from flask import Blueprint
from controller.encode_base64 import *
from controller.decode_base64 import *

blueprint = Blueprint('blueprint', __name__)

#ENCODE A PDF TO BASE64 (READ & WRITE)
blueprint.route('/encode/base64', methods=['POST'])(encode_pdf_to_base64_main)
blueprint.route('/decode/base64', methods=['POST'])(decode_base64_to_pdf_main)
blueprint.route('/check/base64', methods=['GET'])(check_to_base64_main)