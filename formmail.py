import config
import StringIO
import formmail
import logging

from google.appengine.api import mail


_REQUEST_KEYS = [
  'first_name',
  'last_name',
  'email',
  'phone_number',
  'contact_method',
  'city',
  'state',
  'areas_of_need',
  'description'
  ]

def SendFormEmail(request):
  dispatch_email = config.ReadConfig('dispatch.email')

  if not dispatch_email:
    logging.info('Dispatch email config not found. Would have sent email here')
    for key in _REQUEST_KEYS:
      logging.info('%s: %s' % (key, ', '.join(request.get_all(key))))
    return None

  logging.info('Sending email to ', dispatch_email)

  subject = GenerateSubject(request)
  body = GenerateEmail(request)

  mail.send_mail(
      sender=dispatch_email,
      to=dispatch_email,
      subject=subject,
      body=body)


def GenerateSubject(request):
  return 'email form contact: %s %s' % (request.get('first_name'), request.get('last_name'))


def GenerateEmail(request):
  buf = StringIO.StringIO()

  for key in _REQUEST_KEYS:
    buf.write('%s:\n' % key)
    buf.write(', '.join(request.get_all(key)))
    buf.write('\n\n')

  return buf.getvalue()
