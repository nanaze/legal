import os
import jinja2
import config
import webapp2
import logging
import formmail


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




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
    formmail.SendFormEmail(self.request)

