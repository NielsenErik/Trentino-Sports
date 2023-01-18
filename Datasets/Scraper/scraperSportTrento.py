import scrapy
from scrapy.http import Request
import time
class MySpider(scrapy.Spider):
    name = 'facilities'
    allowed_domains = ['comune.trento.it', 'www.comune.trento.it']
    start_urls = ['https://www.comune.trento.it/Aree-tematiche/Sport/Associazioni/', 'https://www.comune.trento.it/Aree-tematiche/Sport/Associazioni/(offset)/20', 'https://www.comune.trento.it/Aree-tematiche/Sport/Associazioni/(offset)/30', 'https://www.comune.trento.it/Aree-tematiche/Sport/Associazioni/(offset)/40']
    def parse(self, response):
        self.logger.info("[MAIN DOMAIN] Working...")
        i = 0
        self.logger.info('[MAIN DOMAIN] Response from %s arrived', response.url)
        for a in response.css('div.media-body'):
            fac = dict(
                title = a.css("h3 a::text").get().strip(),
                link= a.css("h3 a::attr(href)").get()
            )
            self.logger.info("[MAIN DOMAIN] Done")
            yield Request(fac["link"], callback=self.parse_facilities, cb_kwargs=dict(facility = fac))
        
    
    def parse_facilities(self, response, facility):
        self.logger.info('[SUB DOMAIN] Response from %s arrived', response.url)
        self.logger.info("[SUB DOMAIN] Working...")
        facility["infos"] = []
        fac = {}
        
        for info in response.css(".panel-body .row"):
            k = info.css('strong::text').get().strip()
            s = info.css('div.col-md-10::text').get().strip()
            fac[k]=s

        for info in response.css(".content-detail .row"):
            k = info.css('.col-md-3 strong::text').get().strip()
            s = info.css('.col-md-9::text').get()
            fac[k]=s
        
        facility["infos"] = fac
                
        
        facility["infos"] = fac
        yield facility
