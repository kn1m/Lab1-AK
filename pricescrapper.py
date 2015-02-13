__author__ = 'kn1m'

import os
import xml.etree.ElementTree as ET
from urllib2 import Request, urlopen, URLError, HTTPError
from lxml import etree, html
from xml.dom import minidom
import re


class PriceScrapper(object):

    def __init__(self, input_path, output_path):
        if os.path.exists(input_path):
            if not os.path.isfile(input_path):
                raise IOError("Not a file: %s" % input_path)
        else:
            raise IOError("File not found: %s" % input_path)

        self.input_path = input_path
        self.output_path = output_path

    def get_urls_from_xml(self):
        urls = []
        tree = ET.parse(self.input_path)
        root = tree.getroot()
        for child in root:
            # using regexp to remove whitespace from line, for better output later
            line = child.text
            line = re.sub('[\n\t ]', '', line)
            urls.append(line)
        return urls

    def get_tags_from_xml(self):
        xml_doc = minidom.parse(self.input_path)
        item_list = xml_doc.getElementsByTagName('url')
        for s in item_list :
            print s.attributes['maintag'].value
            print s.attributes['tag'].value
            print s.attributes['name'].value


    def scrapper(self, resources):
        self.output_list = []
        for resource in resources:
            try:
                test_req = urlopen(resource).read()
            except HTTPError as e:
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
            except URLError as e:
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            else:
                # everything is fine
                #page = requests.get(resource)
                #tree = html.fromstring(page.text)
                div = 'div'
                tree = html.fromstring(test_req)
                #prices = tree.xpath('//' + div + '[@id="product_price_body"]/text()')
                prices = tree.xpath('//%s[@id="product_price_body"]/text()' % div)
                for price in prices:
                    pricez = ''.join(x for x in price if x.isdigit())
                    print int(pricez)


    def write_xml(self):
        products = ET.Element("products")
        product = ET.SubElement(products, "product")

        #XML writing tests
        ET.SubElement(product, "product_name", name="blah").text = "some value1"
        ET.SubElement(product, "lover_price", name="asdfasd").text = "some vlaue2"
        ET.SubElement(product, "higher_price", name="asdfdasd").text = "some vlaue2"

        tree = ET.ElementTree(products)
        tree.write(self.output_path)

        parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
        document = etree.parse(self.output_path, parser)
        document.write(self.output_path, pretty_print=True, encoding='utf-8')

    @property
    def set_output_path(self, output_path):
        self.output_path = output_path

    @property
    def set_input_path(self, input_path):
        self.input_path = input_path

    @staticmethod
    def call_levenstein(s1,s2):
        n = range(0, len(s1)+1)
        for y in xrange(1,len(s2)+1):
            l,n = n,[y]
            for x in xrange(1,len(s1)+1):
                n.append(min(l[x]+1,n[-1]+1,l[x-1]+((s2[y-1]!=s1[x-1]) and 1 or 0)))
        return n[-1]












