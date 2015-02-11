
from urllib2 import Request, urlopen, URLError, HTTPError
from xml.dom import minidom


def xml_parse():
    xmldoc = minidom.parse('urls.xml')
    itemlist = xmldoc.getElementsByTagName('url')
    print len(itemlist)
    print itemlist[0].attributes['name'].value
    for s in itemlist:
        print s.attributes['name'].value


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


xml_parse()
make_request()