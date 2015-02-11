
from urllib2 import Request, urlopen, URLError, HTTPError
import xml.etree.ElementTree as ET
import os

def xml_parse(path):
    if os.path.exists(path):
        if not os.path.isfile(path):
            raise IOError("not a file: %s" % path)
    else:
        raise IOError("file not found: %s" % path)
    urls = []
    tree = ET.parse(path)
    root = tree.getroot()
    for child in root:
        urls.append(child.text)
    return urls



def make_request():
    req = Request('http://www.voidspace.org.uk')
    try:
        response = urlopen(req)
    except HTTPError as e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError as e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    else:
        # everything is fine
        print 'Well done, comrade!'

def main():
    urls = xml_parse('urls.xml')
    for url in urls:
        print url
    make_request()

main()