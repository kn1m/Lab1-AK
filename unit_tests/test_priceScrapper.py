from unittest import TestCase
from pricescrapper import PriceScrapper

__author__ = 'kn1m'


class TestPriceScrapper(TestCase):
    def test_get_urls_from_xml(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertEqual(s.get_urls_from_xml(), ['http://koba.ua/product/noutbuk_dell_inspiron_3542_156_intel_i3-4005u_4500dvdintwifibtlin_59256/',
                                               'http://elmir.ua/laptops/notebook_dell_inspiron_3542_black_i35345dil-34.html?utm_campaign=%D0%9D%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8%2C%20%D1%83%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D0%B1%D1%83%D0%BA%D0%B8&utm_content=256258&utm_medium=cpc&utm_source=hotline&utm_term=Dell%20Inspiron%203542%20%28I35345DIL-34%29',
                                               'http://allo.ua/ru/products/notebooks/dell-inspiron-3542-i35345dil-34.html?utm_medium=price_list&utm_source=hotline&utm_term=dell_inspiron_3542_i35345dil_34&utm_campaign=hotline_noutbuki',
                                               'http://allo.ua/ru/products/mobile/sony-xperia-z1-c6902-black.html',
                                               'http://all-ok.com.ua/mobilnye-telefony/sony-xperia-z1-c6902-black-detail.html?utm_medium=cpc&utm_source=hotline&utm_campaign=%D1%EC%E0%F0%F2%F4%EE%ED%FB+%E8+%EC%EE%E1%E8%EB%FC%ED%FB%E5+%F2%E5%EB%E5%F4%EE%ED%FB&utm_content=&utm_term=Sony+Xperia+Z1+C6902+%28Black%29',
                                               'http://musicmag.com.ua/audioquest-vodka-hdmi-2m.html'])

    def test_get_tags_from_xml(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertEqual(s.get_tags_from_xml(), [[u'div', u'id', u'product_price_body'],
                                               [u'span', u'itemprop', u'price'],
                                               [u'span', u'class', u'sum'],
                                               [u'span', u'class', u'sum'],
                                               [u'span', u'class', u'PricesalesPrice'],
                                               [u'span', u'class', u'price']])

    def test_scrapper(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertEqual(s.scrapper([]), None)

    def test_levenshtein(self):
        s = PriceScrapper('../urls.xml', 'res.xml')
        self.assertEqual(s.levenshtein('asd', 'not'), 3)