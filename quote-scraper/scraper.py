import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "quote-spider"
    start_urls = [
        'http://quotes.toscrape.com']
    scraped_data = []
    
    def parse(self, response, scraped_data=scraped_data):
        QUOTE_SELECTOR = '.quote'
        TEXT_SELECTOR = '.text::text'
        AUTHOR_SELECTOR = '.author::text'
        ABOUT_SELECTOR = '.author + a::attr(href)'
        TAG_SELECTOR = '.tags > .tag::text'
        NEXT_SELECTOR = '.next a::attr(href)'

        for quote in response.css(QUOTE_SELECTOR):
            data = {
                'quote': quote.css(TEXT_SELECTOR).extract_first(),
                'author': quote.css(AUTHOR_SELECTOR).extract_first(),
                'about': "https://quotes.toscrape.com" + quote.css(ABOUT_SELECTOR).extract_first(),
                'tags': quote.css(TAG_SELECTOR).extract()
            }
            scraped_data.append(data)
        
        with open('quotes.json', 'w') as json_file:
            json.dump(scraped_data, json_file, indent=4)

        next_page = response.css(NEXT_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page)
                )