from scrapy.spider import Spider
from scrapy.selector import Selector

from uksw.items import Website


class EcolexSpider(Spider):
    name = "ecolex"
    allowed_domains = ["www.ecolex.org"]
    start_urls = [
        "http://www.ecolex.org/ecolex/ledge/view/SearchResults;DIDPFDSIjsessionid=A4AEFE4145473BF69935AA6AF2A46BD6?screen=Common&listingField=&allFields=&allFields_allWords=allWords&titleOfText=&titleOfText_allWords=allWords&subject=&subject_allWords=allWords&country=&country_allWords=allWords&region=&region_allWords=allWords&basin=&basin_allWords=allWords&keyword=&keyword_allWords=allWords&languageOfDocument=&languageOfDocument_allWords=allWords&searchDate_start=1960&searchDate_end=2014&sortField=searchDate",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items
