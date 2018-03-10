# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy.spiders import Spider

from bugzilla.items import BugItem, CommentItem


class ChainsawSpider(Spider):
    name = 'chainsaw'
    allowed_domains = ['bz.apache.org']
    bug_list = [
        '40068',
        '40472',
        '40533',
        '47208',
        '48607',
        '49421',
        '49489',
        '50433',
        '50445',
        '51227',
        '51538',
        '52765',
        '54335',
        '56142',
        '57487',
        '57881',
        '29305',
        '30892',
        '31089',
        '38582',
        '43736',
        '31179',
        '42883',
        '34738',
        '35239',
        '46573',
        '26084',
        '29244',
        '30888',
        '31178'
    ]
    start_urls = [f'https://bz.apache.org/bugzilla/show_bug.cgi?id={bug_id}&ctype=xml' for bug_id in bug_list]

    def parse(self, response):
        selector = Selector(response)
        bug_item = self.parse_bug(selector)
        self.log(bug_item)
        yield bug_item
        for comment_selector in selector.xpath('//long_desc'):
            yield self.parse_comment(comment_selector, bug_item['bug_id'])

    @staticmethod
    def parse_bug(selector):
        bug_id = selector.xpath('//bug_id/text()').extract_first()
        summary = selector.xpath('//short_desc/text()').extract_first()
        reporter = selector.xpath('//reporter/@name').extract_first()
        version = selector.xpath('//version/text()').extract_first()
        bug_item = BugItem(bug_id=bug_id, summary=summary, reporter=reporter, version=version)
        return bug_item

    @staticmethod
    def parse_comment(selector, bug_id):
        comment_id = selector.xpath('//commentid/text()').extract_first()
        who = selector.xpath('//who/@name').extract_first()
        text = selector.xpath('//thetext/text()').extract_first()
        comment_item = CommentItem(comment_id=comment_id, bug_id=bug_id, who=who, text=text)
        return comment_item
