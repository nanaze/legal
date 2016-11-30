import cloudstorage
import logging
import os

from google.appengine.api import app_identity

def _GetBucketPath():
  return os.path.join('/', app_identity.get_default_gcs_bucket_name())

def _GetConfigPath():
  return os.path.join(_GetBucketPath(), 'appengine_config')

def _GetValuePath(filename):
  return os.path.join(_GetConfigPath(), filename)

def ReadConfig(filename):
  path = _GetValuePath(filename)

  try:
    with cloudstorage.open(path) as f:
      return f.read()
  except cloudstorage.NotFoundError as e:
    logging.warning('Could not open path %s. %s', path, e)

  return None


