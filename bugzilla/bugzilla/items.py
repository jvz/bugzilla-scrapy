# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class BugItem(Item):
    bug_id = Field()
    summary = Field()
    reporter = Field()
    version = Field()


class CommentItem(Item):
    comment_id = Field()
    bug_id = Field()
    who = Field()
    text = Field()
