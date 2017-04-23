import unirest
import json
import requests
import os
import subprocess
import time
import argparse

rootUrl = "https://api.unsplash.com/"

unirest.default_header("Accept", "application/json")
unirest.default_header("Accept-Version", "v1")
unirest.default_header("Authorization","Client-ID b217110d6cd594306353183c78a86089afc6be2c78a5cf85defec4d7af70930d")

def downloadPic(randomPic_response):
    content = randomPic_response.body
    print 'getting an amazing photo from Unsplash by %s ' % content["user"]["username"]
    picData = requests.get(randomPic_response.body["urls"]["regular"]).content#, callback=applyWallpaper)#.body["urls"]["regular"]
    applyWallpaper(picData)

def applyWallpaper(picStream):
    path = os.path.expanduser('~')+'/.tempWallpaper.jpg'
    with open(path, 'wb') as handler:
        print "saving"
        handler.write(picStream)
        print "enjoy your new wallpaper."
        os.system('gsettings set org.gnome.desktop.background picture-uri file:///%s' % path)

while True:
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='int', type=int, help='time between wallpaper change (in seconds)')
    args = parser.parse_args()
    print "waiting for %s seconds" % args.integers
    time.sleep(args.integers)
    downloadPic(unirest.get(rootUrl + "photos/random", params={"orientation":"landscape"}))#.body["id"]
