from google.appengine.ext import blobstore
import os
import logging 

def _GetBlobstorePath(filename):
  return os.path.join('appengine_config', filename)

def ReadConfig(filename):
  path = _GetBlobstorePath(filename)
  try:
    with blobstore.BlobReader(path) as reader:
      return reader.read()
  except blobstore.BlobNotFoundError:
    logging.info('Could not find config value for key: "%s"', filename)
    return None

