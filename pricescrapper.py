
import xml.etree.ElementTree as ET
from urllib2 import urlopen, URLError, HTTPError
from lxml import etree, html
from xml.dom import minidom
import re
from stringparser import StringParser
import os
import gevent


class PriceScrapper(object):

    def __init__(self, input_path, output_path):
        if os.path.exists(input_path):
            if not os.path.isfile(input_path):
                raise IOError("Not a file: %s" % input_path)
        else:
            raise IOError("File not found: %s" % input_path)

        self.input_path = input_path
        self.output_path = output_path
        self.tags = []
        self.output_list = []
        self.finalized_list = []

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
        for s in item_list:
            temporary = []
            temporary.append(s.attributes['maintag'].value)
            temporary.append(s.attributes['tag'].value)
            temporary.append(s.attributes['name'].value)
            self.tags.append(temporary)
        return self.tags

    def scrapper(self, resources):
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
                tree = html.fromstring(test_req)
                # getting product name
                name = tree.xpath('//title/text()')
                str_parser = StringParser(string=name[0])
                new = str_parser.parse_product_name()

                temporary = []
                temporary.append(new)

                # getting prices
                for tag in self.tags:
                    prices = tree.xpath('//%s[@%s="%s"]/text()' % (tag[0], tag[1], tag[2]))
                    for price in prices:
                        price_curr = ''.join(x for x in price if x.isdigit())
                        temporary.append(price_curr)
                self.output_list.append(temporary)

    def write_xml(self):
        products = ET.Element("products")

        for product_curr in self.finalized_list:
            product = ET.SubElement(products, "product")
            ET.SubElement(product, "product_name").text = product_curr[0]
            ET.SubElement(product, "lover_price").text = min(product_curr[1])
            ET.SubElement(product, "higher_price").text = max(product_curr[1])

        tree = ET.ElementTree(products)
        tree.write(self.output_path)
        parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
        document = etree.parse(self.output_path, parser)
        document.write(self.output_path, pretty_print=True, encoding='utf-8')

    def levenshtein(self, s1, s2):
        cur = self
        if len(s1) < len(s2):
            return cur.levenshtein(s2, s1)
        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def finalize_result(self):
        cur = self
        for first_product in self.output_list:
            for second_product in self.output_list:
                # using Levenshtein distance algo to compare product names
                    if cur.levenshtein(first_product[0], second_product[0]) < 15:
                        fp = first_product[0].split()
                        sp = second_product[0].split()

                        final_product_name = ''

                        # taking same words from both lists and creating new word w/ delimiters removing
                        for f in fp:
                            for s in sp:
                                if str(s) == str(f) and len(s) > 1 and len(f) > 1:
                                    final_product_name += s + ' '

                        first_product[0] = final_product_name
                        second_product[0] = final_product_name

        mark = False

        for p in self.output_list:
            for s in self.finalized_list:
                if s[0] == p[0]:
                    mark = True
            if mark:
                mark = False
                continue
            temp = []
            temp.append(p[0])
            plist = []
            for np in self.output_list:

                plist.append(p[1])
                if np[0] == temp[0]:
                    plist.append(np[1])
            temp.append(plist)
            self.finalized_list.append(temp)

    def multitask_scrapper(self, resources):
        data = []
        for url in resources:
            temporary = []
            temporary.append(url)
            data.append(temporary)
        jobs = [gevent.spawn(self.scrapper, d) for d in data]
        gevent.wait(jobs)
        #results = [g.value for g in jobs]
        #return results


