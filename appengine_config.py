import os
import site

app_path = os.path.dirname(__file__)
third_party_path = os.path.join(app_path, 'third_party')

# Add path for Google Cloud Storage client
gcs_client_path = os.path.join(third_party_path,
                               'appengine-gcs-client/python/src/')

site.addsitedir(gcs_client_path)
