import handlers
import jinja2
import logging
import os
import webapp2
import contact

logging.basicConfig(level=logging.INFO)

server = os.environ['SERVER_SOFTWARE']

is_debug = 'Develop' in server

app = webapp2.WSGIApplication([
  ('/', handlers.MainPage),
  ('/resources', handlers.Resources),
  ('/contact', contact.Contact),
  ('/form', handlers.Form),
  ('/thanks', handlers.Thanks)
], debug=is_debug)
