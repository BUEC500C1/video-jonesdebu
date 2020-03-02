import tweepy
from PIL import Image, ImageDraw, ImageFont
import os
from time import sleep
import imageio
import requests
from io import BytesIO
import wget
import shutil
import cv2
import numpy as np
import glob
import configparser
import base64
import textwrap

#   using code provided by Stefan as a guide for keys file parsing and exception handling:
#   https://github.com/BUEC500C1/video-djtrinh/blob/71cbafb28eb6f86e4c59aacd63b3ee9b458a3032/twitter_api.py#L5
## TODO:
#   1.  get twitter feed using old twitter api from last homework assignment
#   2.  convert text from feed to image
#   3. display images as a video

# User requires consumer_key, consumer_secret, key, secret, and userid

def create_api(path):
    #OAuthHandler and configparser
    config = configparser.ConfigParser()
    config.read(path)
    auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
    auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_secret').strip())
    api = tweepy.API(auth)
    return api



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
def vid_creator(images, dir_name, vid_name):
#If the media folder does not exist create it
    if os.path.isdir(dir_name) is False: #Shouldnt this be is False then directory does not exist so make the directory?
        os.mkdir(dir_name)
    elif os.path.isdir(dir_name) is True:
        print("Directory already exists. Media will be added to the existing directory of the same name")

    if '.avi' not in vid_name:
        vid_name = vid_name + '.avi'
        return

#downlaod images and move them to the media folder
    count = 0
    array_len = len(images)
    for index in range(array_len):
        if images[index].find('http://') == 0: # entry is a media_url with http:// at the beginning of the string
            img_filename = wget.download(images[index])
            if os.path.isfile(str(dir_name) + '/' + str(img_filename)) is False:
                shutil.move(img_filename, dir_name)
            else:
                os.remove(img_filename)

        else:
            #convert text to image using base64 and PIL Image module, save file, and move it to the media folder
            background = Image.new('RGBA', (1024, 768), (255, 255, 255, 255))
            #font = ImageFont.truetype(r'font/Arial.ttf', 14)
            draw = ImageDraw.Draw(background)
            lines = textwrap.wrap(images[index], width=120)
            x, y = 50, 225
            for line in lines:
                draw.text(((x), y), line, font=None, fill="black")
                y += 15

            if os.path.isfile(str(dir_name) + '/' + str(images[index])):
                background.save(str(images[index]) + str(count) + '.png')
                shutil.move(str(images[index]) + str(count) + '.png', dir_name)
                count+=1

            else:
                background.save(str(images[index]) + '.png')
                shutil.move(str(images[index]) + '.png', dir_name)



    #outside of the loop create the video, display it, then delete the media directory for clean up
    img_array = []
    #file_types = ('*.jpg', '*.png')
    for filename in glob.glob(str(dir_name) + '/*.jpg') or glob.glob(str(dir_name) + '/*.png') or glob.glob(str(dir_name) + '/*.gif'):
        img = cv2.imread(filename)
        img = cv2.resize(img, (1920,1080))
        img_array.append(img)

#create video
    if os.path.isfile(str(dir_name) + '/' + str(vid_name)) is False:
        out = cv2.VideoWriter(vid_name, cv2.VideoWriter_fourcc(*'DIVX'), 3, (1920,1080))

    else:
        print('WARNING: video already exists and will be overwritten')
        os.remove(str(dir_name) + '/' + str(vid_name))
        out = cv2.VideoWriter(vid_name, cv2.VideoWriter_fourcc(*'DIVX'), 3, (1920,1080))

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    shutil.move(vid_name, dir_name)

    sleep ( 3 )
    #shutil.rmtree('media')


api = create_api("keys")

#test to put in pytest
images = user_images(api, 'Donovan01060515')
print(len(images))



vid_creator(images, 'media', 'my_vid.avi')
