import tweepy

## TODO:
#   1.  get twitter feed using old twitter api from last homework assignment
#   2.  convert text from feed to image
#   3. display images as a video

# User requires consumer_key, consumer_secret, key, secret, and userid

#def init_keys(consumer_key, consumer_secret, key, secret):
    #OuthHandler
    consumer_key = 'JBuEXV3EgqbsgIe2PUQf9YtRy'
    consumer_secret = 'AaoIK1QkznGO9pfasUnVMzzaWExPQGvO1QWtDcmdgB9wdkWel7'
    key = '1222366331825090560-YzbK3HyrVsr1Cp0JtNY2k88ttegIJN'
    secret = 'v6gQMToztBiD5nEwNLoNIkxqlqBVVm5nkoVWTFwtv78Y5'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    self.api = tweepy.API(auth)

def user_images(consumer_key, consumer_secret, key, secret, userid):
    images = []
    try:
