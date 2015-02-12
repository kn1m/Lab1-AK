__author__ = 'm3sc4'


import HTMLParser

class ProperParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

    def result_list(self):
        return self.parsed_list