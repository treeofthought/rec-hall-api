import unittest
from base64 import b64encode
from flask import current_app
from app import create_app


class BasicsTestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.client = self.app.test_client(use_cookies=True)

  def tearDown(self):
    self.app_context.pop()

  def create_auth_header(self, key):
    auth_value = '{}:{}'.format(key, '')
    creds = b64encode(bytes(auth_value, encoding='utf-8')).decode('utf-8')
    headers = {"Authorization": "Basic {}".format(creds)}
    return headers

  def test_app_exists(self):
      self.assertFalse(current_app is None)

  def test_app_is_testing(self):
    self.assertTrue(current_app.config['TESTING'])

  def test_basic_auth(self):
    # No header
    response = self.client.get('/')
    self.assertEqual(response.status_code, 401)

    # Wrong key
    header = self.create_auth_header('absent')
    response = self.client.get('/', headers=header)
    self.assertEqual(response.status_code, 401)

    # Right key
    header = self.create_auth_header('present')
    response = self.client.get('/', headers=header)
    self.assertEqual(response.status_code, 200)
