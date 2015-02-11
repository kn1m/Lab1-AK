
from pricescrapper import PriceScrapper

'''
def xml_parse(path):
    if os.path.exists(path):
        if not os.path.isfile(path):
            raise IOError("Not a file: %s" % path)
    else:
        raise IOError("File not found: %s" % path)

    urls = []
    tree = ET.parse(path)
    root = tree.getroot()
    for child in root:
        urls.append(child.text)
    return urls


def levenstein_algo(s1,s2):
    n = range(0,len(s1)+1)
    for y in xrange(1,len(s2)+1):
        l,n = n,[y]
        for x in xrange(1,len(s1)+1):
            n.append(min(l[x]+1,n[-1]+1,l[x-1]+((s2[y-1]!=s1[x-1]) and 1 or 0)))
    return n[-1]
'''


'''
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
'''

def main():
    scrappy = PriceScrapper(input_path='urls.xml', output_path='res.xml')
    list = scrappy.parse_xml()
    for url in list:
        print url

    scrappy.write_xml()


main()