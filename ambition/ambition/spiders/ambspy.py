import scrapy
from ..items import AmbitionItem


class AmbspySpider(scrapy.Spider):
    name = "ambspy"
    allowed_domains = ["ambitionbox.com"]
    start_urls = [f"https://www.ambitionbox.com/list-of-companies?page={i}"for i in range(1,501)]
    
    def parse(self, response):
        prods = response.css('div.companyCardWrapper')
        for prod in prods:
            act_link = prod.css('meta[itemprop="url"]::attr(content)').get()
            if act_link:
                yield response.follow(act_link, callback=self.comp_parse)

    def comp_parse(self, response):
        item = AmbitionItem()
        table_tcs = response.css('ul.aboutTable li.aboutItem')

        item['company_name'] = response.css('h1.newHInfo__cNtxt::text').get()
        item['ratings'] = response.css('span.newHInfo__rating::text').get()
        item['nob'] = table_tcs[9].css('a.aboutItem__link::text').get()
        item['toc'] = table_tcs[8].css('a.aboutItem__link::text').get()
        item['ceo'] = table_tcs[6].css('p.textItem__val::text').get() 
        item['ownership'] = table_tcs[1].css('a.aboutItem__link::text').get() 
        item['headquarters'] = table_tcs[4].css('a.aboutItem__link::text').get() 
        item['founded_in'] = table_tcs[0].css('p.textItem__val::text').get()
        item['ccn'] = table_tcs[11].css(
            'a.aboutItem__link::text').get() 
        item['description'] = response.css('div.description::text').get()

        yield item
                                        