import scrapy
from scrapy.http import Request
class MySpider(scrapy.Spider):
    name = 'facilities'
    allowed_domains = ['www.comune.arco.tn.it', 'comune.arco.tn.it']
    start_urls = ['https://www.comune.arco.tn.it/Territorio/Informazioni-utili/Sport/Impianti-Sportivi']
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
        for info in response.xpath('//div[@class="content-detail-item withLabel"]'):
            k = info.css('strong::text').get()
            s = info.css('.Prose::text').get().strip()
            z = info.css('.Prose a::text').get()
            
            if(z == None):
                fac[k]=s
            else:
                fac[k]=z
                
        
        facility["infos"] = fac
        yield facility

        