import cloudstorage
import os
import logging 

def _GetBlobstorePath(filename):
  return os.path.join('appengine_config', filename)

def ReadConfig(filename):
  print dir(cloudstorage)

