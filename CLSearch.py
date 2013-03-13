import urllib2
import time
from bs4 import BeautifulSoup


#----

def get_url(query,rentmin,rentmax,rooms):
##  if query == None:
##    query = ''
##  else:
##    query = query.replace(' ','+')
##  if rentmin == None:
##    rentmin = ''
##  if rentmax == None:
##    rentmax = ''
##  if rooms == None:
##    rooms = ''
##  
##  url = 'http://seattle.craigslist.org/search/apa?zoomToPosting=&altView=&query='+query+'&srchType=A&minAsk='+rentmin+'&maxAsk='+rentmax+'&bedrooms='+rooms
  url = 'http://seattle.craigslist.org/apa/'
  return url


def parse_url(url):
  html = urllib2.urlopen(url)
  if html.code == 200:
    parsed = BeautifulSoup(html)
    return parsed
  else:
    raise IOError('reading %s failed with code %s' % (url, html.code))


def find_lat_long(data):
  lat = data.attrs.get('data-latitude', None)
  lng = data.attrs.get('data-longitude', None)
  if lat and lng:
    return lat,lng


def find_header(data):
  try:
    result = data.find('span', class_='itemph').text.strip()
  except:
    result = ''
  return result


def find_neighborhood(data):
  try:
    result = data.find('span', class_='itempn').text.strip()
  except:
    result = ''
  return result


def find_postURL(data):
  try:
    anchor = data.find('a')
    result = anchor.attrs['href']
  except:
    result = ''
  return result


def find_title(data):
  try:
    anchor = data.find('a')
    result = anchor.text.strip()
  except:
    result = ''
  return result


def has_lat_long(entry):
  a, b = '0', '0'
  a,b = find_lat_long(entry)
  if a !='0' and b != '0':
    return True
  else:
    return False

def parse_posts(posts):
  postList = []
  resultList = []
  counter = 0  

  for entry in posts:
    if has_lat_long(entry):
      try:
        tmpDict = {}
        tmpDict['loc_lat'], tmpDict['loc_long'] = find_lat_long(entry)
        tmpDict['header'] = find_header(entry)
        tmpDict['title'] = find_title(entry)
        tmpDict['neighborhood'] = find_neighborhood(entry)
        tmpDict['post_url'] = find_postURL(entry)
        counter += 1
        tmpDict['ID'] = counter    
        resultList += tmpDict,
      except:
        continue
      
  return resultList


def get_list(query,rentmin,rentmax,rooms):
  resultList = []
  url = get_url(query,rentmin,rentmax,rooms)
  parsed = parse_url(url)
  posts = parsed.find_all('p', class_='row')
  resultList = parse_posts(posts)
  return resultList
