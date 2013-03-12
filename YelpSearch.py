import urllib2
import json
import oauth2

def yelp_search(loc_lat,loc_long,search):

  #adopted from example ***********
  #https://github.com/Yelp/yelp-api/blob/master/v2/python/sign_request.py#

  consumer_key = 'nqWG3SCAY1XXLwgQF1OCbw'
  consumer_secret = 'cRI33I2Heh_s7neiEm9RECMJhhY'
  token = 'MuznJpvCglO598Iioxi6lrvRQruwo6oK'
  token_secret = 'H_TfQb1v1x07o9Te3GSM9YBO9so'

  loc = '&ll=' + str(loc_lat) + ',' + str(loc_long)
  sort = '&sort=0'
  limit = '&limit=2'
  term = '&term=' + search
  
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  url = 'http://api.yelp.com/v2/search?' + term + loc + sort + limit

  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                      'oauth_timestamp': oauth2.generate_timestamp(),
                      'oauth_token': token,
                      'oauth_consumer_key': consumer_key})
  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()

  #*********

  html = urllib2.urlopen(signed_url)
  readData = html.read()
  rawDict = json.loads(readData)
  rawList = rawDict['businesses']

  print '----' + search + ' (Yelp Rating)----'
  for entry in rawList:
    try:
      print entry['name'], '(', entry['rating'],')'
      print '    ' + str(entry['location']['display_address'][0])
    except:
      continue
