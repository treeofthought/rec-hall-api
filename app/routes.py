from flask import Blueprint
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

api = Blueprint('api', __name__)


@auth.verify_password
def verify_password(email_or_token, password):
  if email_or_token == 'present':
    return True
  return False


@api.route('/')
@auth.login_required
def index():
  return ('Hello world!')
