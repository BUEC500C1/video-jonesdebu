import tweepy

## TODO:
#   1.  get twitter feed using old twitter api from last homework assignment
#   2.  convert text from feed to image
#   3. display images as a video

# User requires consumer_key, consumer_secret, key, secret, and userid

def read_image(consumer_key, consumer_secret, key, secret, userid):
    #twitter API OAuth 2 Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)

    #get user timeline for tweets to convert
    user = api.get_user(userid)
    tweets = api.user_timeline(id=userid)

    images_list = [] # list of media_urls
    for status in tweepy.Cursor(api.user_timeline, id=userid).items():
        if 'media' in status.entities:
            for images in status.entities['media']:
                images_list.append(images['media_url'])
        if 'text' in status.entities:
            #convert text to an image and append it to the images_list
