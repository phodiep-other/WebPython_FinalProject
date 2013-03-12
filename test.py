import unittest
import urllib2
from bs4 import BeautifulSoup


class TestFunctions(unittest.TestCase):

    def test_true(self):
        result = 1+1
        assert result == 2

    def test_false(self):
        result = 1+1
        assert result != 3

    def test_CLpost(self):
        filename = 'CLposts.txt'
        #html = urllib2.FileHandler(filename)
        assert True



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
