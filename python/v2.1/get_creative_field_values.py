#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example lists all creative fields.

Tags: creativeFields.list
"""

__author__ = ('api.jimper@gmail.com (Jonathon Imperiosi)')

import argparse
import sys

from apiclient import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'profile_id', type=int,
    help='The ID of the profile to get creative field values for')
argparser.add_argument(
    'field_id', type=int,
    help='The ID of the creative field to get values for')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'dfareporting', 'v2.1', __doc__, __file__, parents=[argparser],
      scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

  profile_id = flags.profile_id
  field_id = flags.field_id

  try:
    # Construct the request.
    request = service.creativeFieldValues().list(
        profileId=profile_id, creativeFieldId=field_id)

    while True:
      # Execute request and print response.
      response = request.execute()

      for value in response['creativeFieldValues']:
        print ('Found creative field value with ID %s and value "%s".'
               % (value['id'], value['value']))

      if response['creativeFieldValues'] and response['nextPageToken']:
        request = service.creativeFieldValues().list_next(request, response)
      else:
        break

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')


if __name__ == '__main__':
  main(sys.argv)
