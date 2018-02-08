from secrets import *

import tweepy
import secrets





    #get authorization
auth = tweepy.OAuthHandler(secrets.consKey, secrets.consSecret)
auth.set_access_token(secrets.accessTokn, secrets.secretAccessTokn)
bot = tweepy.API(auth)
joke = "My boss yelled at me the other day, You’ve got to be the worst train driver in history. How many trains did you derail last year?"
#bot.update_status(joke)

search_text = "#communityservice"
search_number = 2
search_result = bot.search("trump")
#search_result = bot.search(search_text,rpp = search_number)

for i in search_result:
    status = bot.get_status(i.id)
    print(status.text)










