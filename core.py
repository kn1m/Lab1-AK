
from pricescrapper import PriceScrapper
import time


def main():

    conf_file = open('run.conf', "r")
    param = conf_file.readline()
    print 'Program mode: ', param

    scrappy = PriceScrapper(input_path='urls.xml', output_path='res.xml')
    urls = scrappy.get_urls_from_xml()
    for url in urls:
        print url
    scrappy.get_tags_from_xml()

    if param == 'gevent':
        scrappy.multitask_scrapper(urls)
    elif param == 'non-gevent':
        scrappy.scrapper(urls)
    else:
        raise RuntimeError("Unexpected or no mode selected. Check run.conf and select mod: 'gevent' or 'non-gevent'")

start_time = time.time()
main()
print '--- %s seconds ---' % (time.time() - start_time)

