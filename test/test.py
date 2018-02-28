# -*- coding: utf-8 -*-
import scrapy


class StudentNameSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['test.html']

    def parse(self, response):
      yield{
        'a': response.css('#gvshow > tr > td::text').extract()
      }