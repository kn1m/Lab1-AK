__author__ = 'm3sc4'

import os
import xml.etree.ElementTree as ET
from urllib2 import Request, urlopen, URLError, HTTPError
from bs4 import BeautifulSoup
from lxml import etree



class PriceScrapper(object):
    def __init__(self, input_path, output_path):
        if os.path.exists(input_path):
            if not os.path.isfile(input_path):
                raise IOError("Not a file: %s" % input_path)
        else:
            raise IOError("File not found: %s" % input_path)

        self.input_path = input_path
        self.output_path = output_path

    def parse_xml(self):
        urls = []
        tree = ET.parse(self.input_path)
        root = tree.getroot()
        for child in root:
            urls.append(child.text)
        return urls

    def scrapper(self):
        self.output_list = []


    def write_xml(self):
        products = ET.Element("products")
        product = ET.SubElement(products, "product")

        ET.SubElement(product, "product_name", name="blah").text = "some value1"
        ET.SubElement(product, "lover_price", name="asdfasd").text = "some vlaue2"
        ET.SubElement(product, "higher_price", name="asdfdasd").text = "some vlaue2"

        tree = ET.ElementTree(products)
        tree.write(self.output_path)

        parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
        document = etree.parse(self.output_path, parser)
        document.write(self.output_path, pretty_print=True, encoding='utf-8')


















