import config
import StringIO
import formmail
import logging

from google.appengine.api import mail


_REQUEST_KEYS = [
  'email',
  'description'
  ]

def SendFormEmail(request):
  dispatch_email = config.ReadConfig('dispatch.email')

  if not dispatch_email:
    logging.info('Dispatch email config not found. Would have sent email here')
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
  email = request.get('email')
  return 'email form contact: %s' % email


def GenerateEmail(request):
  buf = StringIO.StringIO()

  for key in _REQUEST_KEYS:
    buf.write('%s:\n' % key)
    buf.write(request.get(key))
    buf.write('\n\n')

  return buf.getvalue()
