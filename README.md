## Flickrstagram

python script to be used that can be used as webhook endpoint to upload pictures to instagram (for example from flickr) 

I am using this app in combination with [IFTTT](http://ifttt.com) to upload some of my [flickr pictures](http://flickr.com/bumi) to instagram.

### How does it work

This little flask application exposes an `/flickrstagram` endpoint that accepts a HTTP post request with the following JSON: 

```json
    {
      "source": "your image URL",
      "caption: "the caption of your image",
      "auth": "optional auth code, see configuration"
    }
```

Once received a request the image is processed using [imgix](https://imgix.com/) (you need an account there) to do some [smart cropping](https://docs.imgix.com/apis/url/size/crop) to 1280x1280 pixel which is required by instagram.   
Then the image is uploaded to your instagram using [lukecyca](http://github.com/lukecyca)'s reveres engeneered [instagram python script](https://github.com/lukecyca/python-instagram-upload)

### Installation

    $ pip install -r requirements.txt
    $ [ENV VARS] python hook.py

#### Configuration

the app can be configured using the following environment variables

* IMGIX_HOST: your imgix host. See [imgix sources](https://webapp.imgix.com/sources)
* IMGIX_SIGN_KEY: your imgix signing key. See [imgix sources](https://webapp.imgix.com/sources)
* AUTH: like an API key. can be used to authorize incoming data. If set the incoming JSON request budy must contain this `auth` key ({..., "auth": "your auth env variable"})
* INSTAGRAM_USER: your instagram username
* INSTAGRAM_PASSWORD: your instagram password

#### Deploy to heroku

Simply push to heroku and set your configuration variables. 

-----

Contact: hello@michaelbumann.com   
Blog: [michaelbumann.com](http://michaelbumann.com)  
Twitter: [@bumi](http://twitter.com/bumi)  

