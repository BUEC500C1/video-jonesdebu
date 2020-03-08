# video-jonesdebu
### Twitter API
##  create_api(path)
  * authorizes the dev keys and creates the api object that is used to access the twitter API through tweepy
  * path is the path to the keys file (if the keys file is simply in the same directory then the string "keys" can be entered)

##  user_images(api, username)
  * Gets images and text from a user's timeline and returns an array of media_urls and tweet text depending on the content of the user's user's timeline
  * api is an API created using tweepy.API(auth) which can be done with a create_api function call
  * username is the twitter handle (with the @ sign in front of it) of the user whose timeline you wish to retrieve

## user_tweets(api, username)
  * Gets text based tweets from a user's user's timeline
  * api is an API created using tweepy.API(auth) which can be done with a create_api function call
  * username is the twitter handle (with the @ sign in front of it) of the user whose timeline you wish to retrieve

## vid_creator(images, dir_name, vid_name)
  * creates a video of a user's images and tweet text. The images and text appended to an image is saved to a folder specified by dir_name and the video that is created is specified by vid_name abd is also saved to the directory specified by dir_name
  * images is an array of media_urls and or tweet text that can be retrieved with a user_images function call
  * dir_name is the name of the directory in which you would like to create and save the media retrieved from the timeline and the video specified by vid_name
  * vid_name is the name of the video you would like to create
