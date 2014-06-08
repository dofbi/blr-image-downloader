#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Copyright © 2014 Mamadou Diagne <enova@dofbi.com>

Created on Juin 7, 2014

@author: Mamadou Diagne <genova@dofbi.com>
'''

import pytumblr
import urllib
import os

DOWNLOADED_IMAGE_PATH = "/images/"

CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'

TOKEN='xxxx'
VERIFIER='xxxx'

BLOG = 'xxxx'

TAG = 'xxxx'

client = pytumblr.TumblrRestClient(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    TOKEN,
    VERIFIER,
)
debut = 0

info = client.posts(BLOG,tag=TAG)

Total = info['total_posts']

def download_photo(img_url, filename):
    image_on_web = urllib.urlopen(img_url)
    if image_on_web.headers.maintype == 'image':
        buf = image_on_web.read()
        path = os.getcwd() + DOWNLOADED_IMAGE_PATH
        file_path = "%s%s" % (path, filename)
        downloaded_image = file(file_path, "wb")
        downloaded_image.write(buf)
        downloaded_image.close()
        image_on_web.close()

while debut < Total:
	photos = client.posts(BLOG, type='photo', offset=debut, tag=TAG)
	compte = 0
	for photo in photos['posts']:
  		img_url = photo['photos'][0]['original_size']['url']
  		filename = img_url.split('/')[-1]
  		download_photo(img_url, filename)
  		compte += 1
  	debut = debut + compte
