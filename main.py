import os
import jinja2
import handlers
import webapp2

app = webapp2.WSGIApplication([
  ('/', handlers.MainPage),
  ('/about', handlers.About),
  ('/form', handlers.Form),
], debug=True)
