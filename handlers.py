import os
import jinja2
import webapp2

from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


EMAIL_BODY = """
Email: %s
Description: %s
"""

class MainPage(webapp2.RequestHandler):
  def get(self):

    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    content = template.render({})
    self.response.write(content)

class About(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    content = template.render({})
    self.response.write(content)

class Form(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/form.html')
    content = template.render({})
    self.response.write(content)

  def post(self):
    email = self.request.get('email')
    description = self.request.get('description')
    print('Form recieved')
    print('Email: %s' % email)
    print('Description: %s' % description)
    # TODO(claywoolam): Store an entry in the DB, or figure out a good logging strategy
    print('Sending email to claytest41456@gmail.com')
    mail.send_mail(
        sender="clay.woolam@gmail.com",
        to="claytest41456@gmail.com",
        subject="legal form email",
        body=EMAIL_BODY % (email, description))
