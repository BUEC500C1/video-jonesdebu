import tweepy
from PIL import Image, ImageDraw, ImageFont
import os
import visvis as vv
from time import sleep
import imageio
import requests
from io import BytesIO
import wget
import shutil

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

#get media photos
def user_images(api, username):
    images = []
    try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, count=10, include_entities=True).items():
            if 'media' in tweet.entities:
                for result in tweet.entities['media']:
                    if result['type'] == 'photo':
                        images.append(result['media_url'])
            else:
                images.append(tweet.text)

        return images
    except tweepy.TweepError as error_statement:
        print(error_statement)
        return images

#get text based tweets
def user_tweets(api, username):
    tweets = []
    try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, count=10, include_entities=True, lang="en").items():
            if 'media' in tweet.entities:
                continue # ignore media only want text based tweets here
            tweets.append(tweet.text)
        return tweets
    except tweepy.TweepError as error_statement:
        print(error_statement)
        return tweets

# donwload media move to media folder or convert text to image and move to media folder then use opencv2 Video Writer to create a video use os to open() the video
def vid_creator(images, tweets):
    os.mkdir('media')
    array_len = len(images)
    for index in range(array_len):
        if images[index].find('http://') is 0: # entry is a media_url with http:// at the beginning of the string
            img_filename = wget.download(images[index])
            print(img_filename) # for testing
            shutil.move(img_filename, 'media/' + str(img_filename))
            #im = imageio.imread(images[index])
            #response = requests.get(images[index])
            #img = Image.open(BytesIO(response.content))
            #img.show()
            #sleep( 3 )
        else:
            #convert text to image, save file, and move it to the media folder
    #outside of the loop create the video, display it, then delete the media directory for clean up

    sleep ( 3 )
    shutil.rmtree('media')



#test to put in pytest
images = user_images(api, 'Donovan01060515')
print(len(images))
print(images[1])
print(images[0])


#tweets = user_tweets(api,'Donovan01060515')
#print(len(tweets))
#print(tweets[0])

vid_creator(images, 0)
