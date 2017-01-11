#! /usr/bin/python

import requests
import json
from urlparse import urlparse
import urllib

class User(object):

    def __init__(self):
        self.response_type = 'token'
        
    def read_config():
        with open('config.json') as json_data:
            self.username = json_data["username"]
            self.client_id = json_data["clientId"]
    
    def get_redirect_uri():
        urllib.urlopen("https://www.beeminder.com/apps/authorize");


# TODO: Set up gui to setup the url
resp = requests.get('https://www.beeminder.com/api/v1/users/aba1731/goals/weight.json?auth_token=7qosphRUcKzV6Y36h4p')

if resp.status_code != 200:

