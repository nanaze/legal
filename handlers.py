import os
import jinja2
import config
import webapp2
import logging

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


    dispatch_email = config.ReadConfig('dispatch.email')

    logging.info('Sending email to %s', email)
    
    if not dispatch_email:
      logging.info('Dispatch email config not found. Would have sent email here')
      return None

    # TODO(claywoolam): Store an entry in the DB, or figure out a good logging strategy

    mail.send_mail(
        sender=dispatch_email,
        to=dispatch_email,
        subject="legal form email",
        body=EMAIL_BODY % (email, description))
