import pytest
from twitter_api import create_api, user_images, vid_creator

def test_user_images():
    api = create_api("keys")
    images = user_images(api, 'Donovan01060515')
    assert len[images] == 2
