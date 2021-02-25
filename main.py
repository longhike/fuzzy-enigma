from auth import FB_TOKEN, TW_BEARER_TOKEN
from fb import Facebook
from tw import Twitter

test_id=2271638589
test_name='ruleofpaw'

def fb_fun(token):
    test = Facebook(token)
    pprint.pp(test.my_info())

def tw_fun(token,username):
    test = Twitter(token)
    print(test.get_tweets(username))

if __name__ == "__main__":
    tw_fun(TW_BEARER_TOKEN,test_id)
    # fb_fun(FB_TOKEN)