import tweepy

#   using code provided by Stefan as a guide for keys file parsing and exception handling:
#   https://github.com/BUEC500C1/video-djtrinh/blob/71cbafb28eb6f86e4c59aacd63b3ee9b458a3032/twitter_api.py#L5
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
    api = tweepy.API(auth)

def user_images(api, username):
    images = []
    try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, count=10, include_entities=TRUE):
            if 'media' in tweet.entities:
                for result in tweet.entities['media']
                    if result['type'] == 'photo':
                        images.append(result['media_url'])
        return images
    except tweepy.TweepError as error_statement
        print(error_statement)
        return images
