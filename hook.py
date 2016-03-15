import flask
import urllib
import os
import imgix
import instagram
import json

from instagram import InstagramSession
from flask import Flask, abort, request, flash, redirect, render_template, url_for, jsonify, got_request_exception

app = Flask(__name__)

@app.route('/flickrstragram', methods=['GET','POST'])
def flickrstragram():
    data = json.loads(request.data)
    url = data['source']
    caption = data['flickr']
    insta = InstagramSession()

    builder = imgix.UrlBuilder(os.environ.get('IMGIX_HOST', ''), sign_key=os.environ.get('IMGIX_SIGN_KEY', ''))
    photo = builder.create_url(url, {'w': 1280, 'h': 1280, 'fit': 'crop', 'crop': 'entropy', 'auto': 'enchance'})
    print "downloading"
    urllib.urlretrieve(photo, 'tmp/image.jpg')

    print "uploading"
    if insta.login(os.environ.get('INSTAGRAM_USER', ''), os.environ.get('INSTAGRAM_PASSWORD', '')):
        media_id = insta.upload_photo('tmp/image.jpg')
        print media_id
        if media_id is not None:
            insta.configure_photo(media_id, caption)
        else:
            print "failed to upload"
    else:
        print "failed to login"
    print "done"
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
