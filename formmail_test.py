import unittest
import formmail
import mock

_EXPECTED_BODY = """\
email:
test@test.com

description:
lorem ipsum

"""

_REQUEST_VALUES = {
  'email': 'test@test.com',
  'description' : 'lorem ipsum'
}

class MockRequest(object):
  def get(self, key):
    if key in _REQUEST_VALUES:
      return _REQUEST_VALUES[key]

    return ''


class FormMailTest(unittest.TestCase):

  def test_RequestGenerateEmail(self):
    self.assertMultiLineEqual(
      _EXPECTED_BODY, 
      formmail.GenerateEmail(MockRequest()))

  def test_RequestGenerateSubject(self):
    self.assertEquals('email form contact: test@test.com',
                      formmail.GenerateSubject(MockRequest()))

if __name__ == '__main__':
    unittest.main()
