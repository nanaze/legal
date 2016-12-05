import handlers
import webapp2

class Contact(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    template = handlers.JINJA_ENVIRONMENT.get_template('form.html')
    template_dict = handlers.GetTemplateDict(self.request, additional_stylesheets=['form.css'])
    content = template.render(template_dict)
    self.response.write(content)
