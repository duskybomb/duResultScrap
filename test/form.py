# -*- coding: utf-8 -*-
import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'du-login'
    login_url = 'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx'
    start_urls = [login_url]

    def parse(self, response):
        # extract the csrf token value
        viewstate = response.css('input[name="__VIEWSTATE"]::attr(value)').extract_first()
        viewstategen = response.css('input[name="__VIEWSTATEGENERATOR"]::attr(value)').extract_first()
        eventvalidation = response.css('input[name="__VIEWSTATEGENERATOR"]::attr(value)').extract_first()
        # create a python dictionary with the form values
        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': viewstate,
            '__VIEWSTATEGENERATOR': viewstategen,
            '__EVENTVALIDATION': eventvalidation,
            'ddlcollege':'312',
            'ddlexamtype':'Semester',
            'ddlexamflag':'UG_SEMESTER_4Y',
            'ddlstream':'SC',
            'ddlcourse':'911',
            'ddlpart':'I',
            'ddlsem':'I',
            'txtrollno':'17312911016',
            'txtname':'har',
            'btnsearch':'Print Score Cart/Transcript'
        }
        # submit a POST request to it
        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        """Parse the main page after the spider is logged in"""
        yield {
            'author_name': response.css('#lblcourse0::text').extract_first(),
        }