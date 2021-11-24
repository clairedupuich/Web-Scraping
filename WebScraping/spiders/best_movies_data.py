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
        item['original_title'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').extract()
        item['date'] = response.xpath('//li[@data-testid="title-details-releasedate"]/div/ul/li/a/text()').extract()
        item['public'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[2]/span/text()').extract()
        item['duration'] = response.xpath('//li[@class="ipc-inline-list__item"]/text()').extract()
        item['genre'] = response.xpath('//div[@class="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL"]/a/span/text()').extract()
        item['synopsis'] = response.xpath('//p[@class="GenresAndPlot__Plot-cum89p-6 bUyrda"]/span[1]/text()').extract()
        item['note'] = response.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()').extract_first()
        item['actors'] = response.xpath('//a[@class="StyledComponents__ActorName-y9ygcu-1 eyqFnv"]/text()').extract()
        item['original_language'] = response.xpath('//li[@data-testid="title-details-languages"]/div/ul/li/a/text()').extract()
        item['original_country'] = response.xpath('//li[@data-testid="title-details-origin"]/div/ul/li/a/text()').extract()

        return item
