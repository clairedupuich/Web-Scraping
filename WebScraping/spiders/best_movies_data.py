import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesDataSpider(CrawlSpider):
    name = 'best_movies_data'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//td[@class="titleColumn"]/a']), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//div[@class="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt"]/h1/text()').extract()
        item['original_title'] = response.xpath('//div[@class="OriginalTitle__OriginalTitleText-jz9bzr-0 llYePj"]/text()').get()
        item['date'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/span/text()').extract()
        item['public'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[2]/span/text()').extract()
        # item['date_of_release'] = response.xpath('//a[@class="xXx date "]/text()').extract()
        # item['directors'] = response.xpath('//a[@class="xXx blue-link"]/text()').extract()
        # item['synopsis'] = response.xpath('//div[@class="content-txt "]/text()').extract()
        # item['tab_data'] = response.xpath('//div[@class="meta-body-item meta-body-info"]/text()').extract()

        return item
