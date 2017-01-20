#! /usr/bin/python

import requests
import json
import time
from requests_oauthlib import OAuth1

class User(object):

    def __init__(self):
        self.redirect_uri = 'https://localhost:8888'
        self.beeminder_url = 'https://www.beeminder.com'
        self.update_interval = 10
        self.goal_name = 'motion_beeminder' # TODO: Remove default?
        self.client_secret = 'eneohgmzm03rrg0dqc2pfwf4j' # TODO: Encrypth this??
        self.client_id = '9t789shu6ognpijfylune8zrt'
        self.diff_since = time.time()

    def get_access_token():
        url = '{}/apps/authorize'.format(self.beeminder_url);
        auth = OAuth1('access_token')
        params = {'client_id': self.client_id, 'redirect_uri': self.redirect_uri, 'response_type': 'token'}
        
        req = requests.get(url, auth=auth, params=params)
        req.raise_for_status()
        
        self.access_token = req.content.access_token
        self.username = req.content.username
            
    def set_goal_name(goal_name):
        params = {'access_token': self.access_token}
        req = requests.get('{}/api/v1/users/me.json'.format(self.beeminder_url), 
                            params=params)
        req.raise_for_status()
        
        if goal_name not in req.content.goals:
            # TODO: Put error handling code
            continue

        self.goal_name = goal_name

    def update_goal(min):
        params = {'goals_filter': self.goal_name, 
                  'access_token': self.access_token, 
                  'diff_since': self.prev_time}
        req = requests.get(
                '{}/api/v1/users/me.json'.format(self.beeminder_url),
                params=params)
        req.raise_for_status()
        
        if req.content.updated_at < time.time():
            self.diff_since = time.time()
            req = requests.put(
                '{}/api/v1/users/me.json'.format(self.beeminder_url),
                data={'goal_name': self.goal_name, 'yaxis': str(min)})
            )
            req.raise_for_status()
        

    
        
        
    







