import scrapy


class RealLombardSpider(scrapy.Spider):
    name = "reallombard"
    allowed_domains = ["http://reallombard.by/sale/"]
    start_urls = ["http://reallombard.by/sale/"]

    def parse(self, response):
        for product in response.css(".product-details"):
            data = {
                "title": product.css("h4 a::text").get(),
                "price": product.css(".price::text").get(),
                "link": product.css(".cart a::attr(href)").get(),
            }
            yield data

        for next_page in response.css(".navigation a:last-child::attr(href)"):
            yield response.follow(next_page, callback=self.parse)
