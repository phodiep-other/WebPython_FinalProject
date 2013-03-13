import unittest
import urllib2
from bs4 import BeautifulSoup

import CLSearch


class TestFunctions(unittest.TestCase):

    def test_true(self):
        result = 1+1
        assert result == 2

    def test_false(self):
        result = 1+1
        assert result != 3

    def test_getEmptyURL(self):
        emptyurl = 'http://seattle.craigslist.org/search/apa?zoomToPosting=&altView=&query=&srchType=A&minAsk=&maxAsk=&bedrooms='
        testurl = CLSearch.get_url('','','','')
        assert emptyurl == testurl

    def test_getURL(self):
        query = 'qa'
        rentmin = '0'
        rentmax = '1000'
        rooms = '1'
        url = 'http://seattle.craigslist.org/search/apa?zoomToPosting=&altView=&query='+query+'&srchType=A&minAsk='+rentmin+'&maxAsk='+rentmax+'&bedrooms='+rooms
        testurl = CLSearch.get_url('qa','0','1000','1')
        assert url == testurl

    def test_emptyList(self):
        emptyList = []
        testList = CLSearch.get_list('none','0','0','100')
        assert emptyList == testList

    def test_getList(self):
        
        assert True

    def test_empty_post(self):
        assert True

    def test_parse_post(self):
        assert True

    def test_lat_long(self):
        assert True

    def test_empty_lat_long(self):
        assert True


##    def test_CLpost(self):
##        filename = 'CLposts.txt'
##        with open(filename,'r') as tempfile:
##            
##        assert True

        

##
##    def test_search_form(self):
##        html = 'http://localhost:8080/'
##        assert urllib2.urlopen(html) == template('search_form.tpl')
    
#create valid list to compare to
#create invalid list to compare to
#mock library
    #pass in CL html (using fileopen in place of openurl)
    # pass in nonCL html

if __name__ == '__main__':
    unittest.main()
