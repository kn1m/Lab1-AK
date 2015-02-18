
from pricescrapper import PriceScrapper

def main():
    scrappy = PriceScrapper(input_path='urls.xml', output_path='res.xml')
    list = scrappy.get_urls_from_xml()
    for url in list:
        print url
    scrappy.get_tags_from_xml()
    scrappy.scrapper(list)
    scrappy.finalize_result()
    scrappy.write_xml()

main()