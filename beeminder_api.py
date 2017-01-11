#! /usr/bin/python

import requests
import json

class User(object):

    def __init__(self):
        self.username = 
        self.base_url = 
        self.response_type = 'token'
        
    def read_config():
        with open('config.json') as json_data:
            self.username = json_data["username"]
            self.client_id = json_data["clientId"]
            self.



# TODO: Set up gui to setup the url
resp = requests.get('https://www.beeminder.com/api/v1/users/aba1731/goals/weight.json?auth_token=7qosphRUcKzV6Y36h4p')

if resp.status_code != 200:

