import scrapy
from scrapy.http import Request
class MySpider(scrapy.Spider):
    name = 'facilities'
    allowed_domains = ['paginegialle.it', 'www.paginegialle.it']
    links = []
    for pages in range(0,4):
        tmp = 'https://www.paginegialle.it/trentino_alto_adige/trento/impianto_sportivo/p-'+str(pages+1)+'.html'
        links.append(tmp)
    start_urls = links
    def parse(self, response):
        self.logger.info("[MAIN DOMAIN] Working...")
        i = 0
        self.logger.info('[MAIN DOMAIN] Response from %s arrived', response.url)
        for a in response.css('div.search-itm__info'):
            fac = dict(
                title = a.css("a h2::text").get().strip(),
                link= a.css("a::attr(href)").get()
            )
            self.logger.info("[MAIN DOMAIN] Done")
            yield Request(fac["link"], callback=self.parse_facilities, cb_kwargs=dict(facility = fac))
        
    
    def parse_facilities(self, response, facility):
        self.logger.info('[SUB DOMAIN] Response from %s arrived', response.url)
        self.logger.info("[SUB DOMAIN] Working...")

        facility["Address"] = []
        facAddress = {}
        for info in response.css(".scheda-azienda__companyTextbox"):
            g = info.css('div.scheda-azienda__companyAddress::text').extract()
            g = [w.replace("\n", "") for w in g]
            g = [w.replace("\r", "") for w in g]
            g = [w.replace("\t", "") for w in g]
            
            facAddress["Address"] = g 
        facility["Address"] = facAddress
        
        facility["Openings"] = []
        fac = {}
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = 0
        for info in response.css('[id="companyHours"] ul li'):
            s = info.css('span.scheda-azienda__tableTime span::text').get().strip()
            fac[days[day]]=s
            day += 1               
        
        facility["Openings"] = fac

        facility["Telephone"] = []
        facTel = {}
        t = info.xpath('//a[@class="bttn bttn--yellowTel bttn--3d  scheda-azienda__cta_phoneButton shinystat_ssxl"]/span[@class="bttn__label"]/text()').get().strip()
        facTel["Telephone"] = t
        facility["Telephone"] = facTel

        facility["Type_of_facility"] = []
        facType = {}
        tipo = info.xpath('//div[@class="scheda-azienda__companyCategory"]/span[@class="bttn__label"]/text()').get().strip()
        facType["Type"] = tipo
        facility["Type_of_facility"] = facType
        yield facility

        