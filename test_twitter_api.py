import pytest
from twitter_api import create_api, user_images, vid_creator

def test_user_images():
    api = create_api("keys")
    images = user_images(api, 'Donovan01060515')
    #This user has 6 items in their timeline so the length of the images_array will be 6.
    assert len(images) == 6

#Test that the video exists
