import scrapy
from scrapy.http import Request
class MySpider(scrapy.Spider):
    name = 'facilities'
    allowed_domains = ['comune.trento.it', 'www.comune.trento.it']
    start_urls = ['https://www.comune.trento.it/Aree-tematiche/Sport/Impianti-sportivi/Impianti-gestiti-da-Asis', 'https://www.comune.trento.it/Aree-tematiche/Sport/Impianti-sportivi/Impianti-gestiti-dal-Comune-e-da-associazioni-sportive']
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
        i = 0
        for info in response.css(".content-detail .row"):
            k = info.css('strong::text').get()
            s = info.css('.col-md-9::text').get().strip()
            z = info.css('.col-md-9 a::text').get()
            
            if(z == None):
                fac[k]=s
            else:
                fac[k]=z
                
        
        facility["infos"] = fac
        yield facility

        