import StringIO

_REQUEST_KEYS = [
  'email',
  'description'
  ]

def GenerateEmail(request):
  buf = StringIO.StringIO()

  for key in _REQUEST_KEYS:
    buf.write('%s:\n' % key)
    buf.write(request.get(key))
    buf.write('\n\n')

  return buf.getvalue()
