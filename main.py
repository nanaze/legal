import webapp2


class MainPage(webapp2.RequestHandler):
  def get(self):

    self.response.headers['Content-Type'] = 'text/plain'

    with open('templates/template.html') as f:
      content = f.read()
      self.response.write(content)

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
