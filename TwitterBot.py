from secrets import *

import tweepy
import secrets


    #get authorization
auth = tweepy.OAuthHandler(secrets.consKey, secrets.consSecret)
auth.set_access_token(secrets.accessTokn, secrets.secretAccessTokn)
bot = tweepy.API(auth)
opportunity = "Anyone looking for volunteer opprtunities in the area"
bot.update_status(opportunity)

search_text = "#communityservice"
search_number = 2
search_result = bot.search(search_text,rpp = search_number)

for i in search_result:
    opportunity = bot.get_status(i.id)
    print(opportunity.text)










