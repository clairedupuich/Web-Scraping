import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestSeriesDataSpider(CrawlSpider):
    name = 'best_series_data'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//td[@class="titleColumn"]/a']), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//div[@class="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt"]/h1/text()').extract()
        item['type'] = response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"]/ul/li[1]/text()').extract()
        item['duration'] = response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"]/ul/li[4]/text()').extract()
        item['genre'] = response.xpath('//div[@class="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL"]/a/span/text()').extract()
        item['synopsis'] = response.xpath('//p[@class="GenresAndPlot__Plot-cum89p-6 bUyrda"]/span[1]/text()').extract()
        item['note'] = response.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()').extract_first()
        item['episode_nb'] = response.xpath('//span[@class="ipc-title__subtext"]/text()').extract_first()
        item['season_nb'] = response.xpath('//div[@class="BrowseEpisodes__BrowseLinksContainer-sc-1a626ql-4 cmwEsB"]/a[2]/div/text()').extract()
        item['date'] = response.xpath('//li[@data-testid="title-details-releasedate"]/div/ul/li/a/text()').extract()
        item['actors'] = response.xpath('//a[@class="StyledComponents__ActorName-y9ygcu-1 eyqFnv"]/text()').extract()
        item['original_language'] = response.xpath('//li[@data-testid="title-details-languages"]/div/ul/li/a/text()').extract()
        item['original_country'] = response.xpath('//li[@data-testid="title-details-origin"]/div/ul/li/a/text()').extract()

        return item