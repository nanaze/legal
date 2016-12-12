import csv
import handlers
import webapp2

def _GetStateCodes():
  with open('data/states.txt') as f:
    for line in f:
      line = line.strip()
      if line:
        yield line

STATE_CODES = sorted(list(_GetStateCodes()))
      
class Contact(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    additional_stylesheets = [
      'form.css',
      'columns.css'
    ]
    
    template = handlers.JINJA_ENVIRONMENT.get_template('contact.html')
    template_dict = handlers.GetTemplateDict(
      self.request,
      additional_stylesheets=additional_stylesheets)

    template_dict['states'] = [''] + STATE_CODES
    
    content = template.render(template_dict)
    self.response.write(content)
