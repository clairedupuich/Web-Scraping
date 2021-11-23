import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies_data'
    allowed_domains = ['allocine.fr']
    start_urls = ['http://www.allocine.fr/film/meilleurs/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//h2[@class="meta-title"]', '//div[@class="pagination-item-holder"]']), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//main[@class="content-layout entity movie cf seance-geoloc-redir"]/div[@class="titlebar titlebar-page"]/div/text()').extract()
        # item['date_of_release'] = response.xpath('//a[@class="xXx date blue-link"]/text()').get()
        # item['duration'] = response.xpath('//div[@class="meta-body-item meta-body-info"]/text()[4]').extract()
        # item['duration'] = item['duration'].strip()
        # item['genre_n_actors'] = response.xpath('//a[contains(@href, "/personne/fichepersonne")]/text()').extract()
        # item['date_of_release'] = response.xpath('//a[@class="xXx date "]/text()').extract()
        # item['directors'] = response.xpath('//a[@class="xXx blue-link"]/text()').extract()
        # item['synopsis'] = response.xpath('//div[@class="content-txt "]/text()').extract()
        # item['tab_data'] = response.xpath('//div[@class="meta-body-item meta-body-info"]/text()').extract()
        
        return item

