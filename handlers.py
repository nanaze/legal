import os
import jinja2
import config
import webapp2
import logging
import formmail
import collections

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

NavigationEntry = collections.namedtuple('NavigationEntry', ['href', 'text'])

def _GetNavigationEntries():
  return [
    NavigationEntry('/', 'What we do.'),
    NavigationEntry('/resources', 'Resources.'),
    NavigationEntry('/contact', 'Contact us.')
  ]

def _GetTemplateDict():
  return {
    'navigation': _GetNavigationEntries()
  }

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    content = template.render(_GetTemplateDict())
    self.response.write(content)

class About(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    content = template.render(_GetTemplateDict())
    self.response.write(content)

class Form(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/form.html')
    content = template.render(_GetTemplateDict())
    self.response.write(content)

  def post(self):
    formmail.SendFormEmail(self.request)

