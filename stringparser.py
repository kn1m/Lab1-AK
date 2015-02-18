__author__ = 'kn1m'

import re


class StringParser(object):

    def __init__(self, string):
        if isinstance(string, basestring):
            self.string = string
        else:
            raise TypeError("Not a string: %s" % string)

    @property
    def get_string(self):
        return self.string

    def parse_product_name(self):
        # removing cyrillic symbols from string
        test = unicode(self.string)
        encoded = test.encode('ascii', 'ignore')
        line = unicode(encoded)

        # removing delimiters and whitespace
        line = re.sub('[\n\t,|.]', '', line)

        # removing repeating words
        words = line.split()
        new = " ".join(sorted(set(words), key=words.index))
        return new