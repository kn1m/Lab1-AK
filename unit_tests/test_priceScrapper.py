from unittest import TestCase
from pricescrapper import PriceScrapper

__author__ = 'kn1m'


class TestPriceScrapper(TestCase):
    def test_get_urls_from_xml(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertRaises(s.get_urls_from_xml)


    def test_get_tags_from_xml(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertRaises(s.get_urls_from_xml)

    def test_scrapper(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertEqual(s.scrapper([]), None)

    def test_levenshtein(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertEqual(s.levenshtein('asd', 'not'), 3)