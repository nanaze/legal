import os
import jinja2
import handlers
import logging
import webapp2

logging.basicConfig(level=logging.INFO)

app = webapp2.WSGIApplication([
  ('/', handlers.MainPage),
  ('/resources', handlers.Resources),
  ('/contact', handlers.Form),
  ('/form', handlers.Form),
], debug=True)
