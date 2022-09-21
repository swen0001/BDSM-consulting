import scrapy


class RezkaFilmSpider(scrapy.Spider):
    name = 'rezka_film'
    allowed_domains = ['rezka.eg']
    start_urls = ['https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').get(),
            'title_eng': response.xpath('//div[@class="b-post__origtitle"]/text()').get(),
            'rating': response.xpath('//span[@class="b-post__info_rates imdb"]//span/text()').get(),
            'country': response.xpath('//h2[text()="Страна"]/following::a/text()').get(),
            'film_time': response.xpath('//td[@itemprop="duration"]/text()').get(),
            'description': response.xpath('//div[@class="b-post__description_text"]/text()').get(),
        }