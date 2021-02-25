import inquirer
from auth import FB_TOKEN, TW_BEARER_TOKEN
from fb import Facebook
from tw import Twitter

test_id=2271638589
test_name='ruleofpaw'

def run():
    start=main_question()
    if start=='quit':
        print('OK, bye!')
        quit()
    elif start=='twitter':
        run_tw()
    elif start=='facebook':
        run_fb()

def run_tw():
    q = [
        inquirer.List('which_tw',
        message='What do you want to find?',
        choices=['user','tweets','quit'])
    ]
    a = inquirer.prompt(q)['which_tw']
    if a=='quit':
        print('OK, bye!')
        quit()
    elif a=='user':
        q_s=[inquirer.Text('username_tw','enter the user\'s username: ')]
        a_s=inquirer.prompt(q_s)['username_tw']
        tw=Twitter(TW_BEARER_TOKEN)
        tw_r=tw.get_user(a_s)
        print(tw_r)
        run_tw()
    elif a=='tweets':
        q_s=[inquirer.Text('user_id_tw','enter the user\'s ID: ')]
        a_s=inquirer.prompt(q_s)['user_id_tw']
        tw=Twitter(TW_BEARER_TOKEN)
        tw_r=tw.get_tweets(a_s)
        print(tw_r)
        run_tw()

def run_fb():
    pass

def main_question():
    q = [
        inquirer.List('which',
        message='From which platform do you want to get data?',
        choices=['facebook','twitter','quit'])
    ]
    a = inquirer.prompt(q)['which']
    return a
