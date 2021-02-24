import requests as R
import json
from auth import TW_BEARER_TOKEN

class Twitter:
    def __init__(self, token):
        self.token=token
        
    def __auth(self):
        return self.token
    
    def __create_headers(self):
        headers = {"Authorization": "Bearer {}".format(self.token)}
        return headers
    
    def __user_make_base_url(self,username):
        return f'https://api.twitter.com/2/users/by?usernames={username}&user.fields=username,description,created_at'

    def __tweets_make_base_url(self,id):
        return "https://api.twitter.com/2/users/{}/tweets".format(id)

    @staticmethod
    def __tweets_make_params():
        return {"tweet.fields": "text"}
    
    @staticmethod
    def __make_request(url, headers, params=None):
        if params:
            response = R.request("GET", url, headers=headers, params=params)
            print(response.status_code)
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(
                        response.status_code, response.text
                    )
                )
            return response.json()
        else:
            response = R.request("GET", url, headers=headers)
            print(response.status_code)
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(
                        response.status_code, response.text
                    )
                )
            return response.json()
    
    def get_tweets(self,id):
        bearer_token = self.__auth()
        url = self.__tweets_make_base_url(id)
        headers = self.__create_headers()
        params = self.__tweets_make_params()
        json_response = self.__make_request(url, headers, params)
        return json.dumps(json_response, indent=4, sort_keys=True)
    
    def get_user(self,username):
        bearer_token = self.__auth()
        url = self.__user_make_base_url(username)
        headers = self.__create_headers()
        json_response = self.__make_request(url, headers)
        return json.dumps(json_response, indent=4, sort_keys=True)
