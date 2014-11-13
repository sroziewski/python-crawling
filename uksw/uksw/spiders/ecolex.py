from scrapy import FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from uksw.items import DataItem

from scrapy.shell import inspect_response

from scrapy.utils.response import open_in_browser

class EcolexSpider(CrawlSpider):
    # ...
    name = "ecolex"
    allowed_domains = ["www.ecolex.org"]

    rules = [
        # Rule(SgmlLinkExtractor(allow=("ecolex/ledge/view/SearchResults?$", )), follow=True),
        Rule(SgmlLinkExtractor(allow=("ecolex/ledge/view/RecordDetails?$", )), callback='found_items'),
    ]

    def start_requests(self):
        return [FormRequest("http://www.ecolex.org/ecolex/ledge/view/Common", formdata={'searchDate_start': '1960'}, callback=self.search_form_clicked)]

    def search_form_clicked(self, response):
    # here you would extract links to follow and return Requests for
    # each of them, with another callback
        yield FormRequest.from_response(response, formnumber=1)


    def found_items(self, response):
        # try scrapping
        item = DataItem()
        hxs = HtmlXPathSelector(response)

        item['title'] =  hxs.select('//table[@class="input-fields"]/tbody/tr[5]/td').extract()
        item['date'] =  hxs.select('//table[@class="input-fields"]/tbody/tr[7]/td').extract()
        item['abstract'] =  hxs.select('//table[@class="input-fields"]/tbody/tr[14]/td').extract()
        item['subject'] =  hxs.select('//table[@class="input-fields"]/tbody/tr[15]/td').extract()
        item['keywords'] =  hxs.select('//table[@class="input-fields"]/tbody/tr[16]/td').extract()
        item['id'] =  hxs.select('//table[@class="input-fields"]/tbody/tr[17]/td').extract()
        # print repr(item).decode("unicode-escape") + '\n'
        # info('parsed ' + str(response))
        return item


