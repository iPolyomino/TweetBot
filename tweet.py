# coding: utf-8

from twython import Twython
import random
import secret

def main():
    APP_KEY = secret.APP_KEY
    APP_SECRET = secret.APP_SECRET
    OAUTH_TOKEN = secret.OAUTH_TOKEN
    OAUTH_TOKEN_SECRET = secret.OAUTH_TOKEN_SECRET

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    kana = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'
    for _ in range(1):
        tweet = ''
        for i in range(random.randint(3,7)):
            tweet += random.choice(list(kana))
        twitter.update_status(status = tweet)

if __name__ == '__main__':
    main()
