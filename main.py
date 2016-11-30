import handlers
import jinja2
import logging
import os
import webapp2

logging.basicConfig(level=logging.INFO)

server = os.environ['SERVER_SOFTWARE']

is_debug = 'Develop' in server

app = webapp2.WSGIApplication([
  ('/', handlers.MainPage),
  ('/resources', handlers.Resources),
  ('/contact', handlers.Contact),
  ('/form', handlers.Form),
], debug=is_debug)
