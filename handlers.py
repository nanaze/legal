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
    trim_blocks=True,
    autoescape=True)

NavigationEntry = collections.namedtuple('NavigationEntry', ['href', 'text'])

def _GetNavigationEntries():
  return [
    NavigationEntry('/', 'What we do.'),
    NavigationEntry('/resources', 'Resources.'),
    NavigationEntry('/contact', 'Contact us.')
  ]

def _GetTemplateDict(request):
  return {
    'navigation': _GetNavigationEntries(),
    'request': request
  }

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    content = template.render(_GetTemplateDict(request))
    self.response.write(content)

class Resources(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    content = template.render(_GetTemplateDict(request))
    self.response.write(content)

class Form(webapp2.RequestHandler):
  def post(self):
    formmail.SendFormEmail(self.request)
    
class Contact(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = JINJA_ENVIRONMENT.get_template('templates/form.html')
    content = template.render(_GetTemplateDict(request))
    self.response.write(content)


