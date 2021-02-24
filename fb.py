import requests as R

class Facebook:
    
    def __init__(self,token,url='https://graph.facebook.com/'):
        self.token=token
        self.url=url
    
    def __set_auth(self):
        return f'access_token={self.token}'

    def my_info(self):
        query='me?fields=id,name&'
        token_string=self.__set_auth()
        return R.get(f'{self.url}{query}{token_string}').json()
    
    def my_posts(self):
        query='me?fields=id,name,posts&'
        token_string=self.__set_auth()
        return R.get(f'{self.url}{query}{token_string}').json()

    def my_friends(self):
        query='me?fields=id,name,friends&'
        token_string=self.__set_auth()
        return R.get(f'{self.url}{query}{token_string}').json()
        