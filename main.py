import scrapy
import csv
from scrapy.crawler import CrawlerProcess
import configparser


class SpidyResults(scrapy.Spider):
    name = 'results'

    config = configparser.RawConfigParser()
    config.read('settings.cfg')
    settings = config['SETTINGS']
    form_dict = {}
    for k, v in settings.items():
        form_dict[k] = v

    form_url = settings['FormUrl']
    start_urls = [settings['StudentNameUrl']]
    download_delay = 1.5

    def parse(self, response):
        resp_list = response.css('#gvshow > tr > td::text').extract()
        self.new_list = []
        i = 0
        while i < len(resp_list):
            if i == 0:
                pass
            elif i % 2 == 1:
                new_sub_list = (resp_list[i], resp_list[i+1])
                self.new_list.append(new_sub_list)
                i = i + 3
            i += 1
        print(self.new_list)
        yield response.follow(self.form_url, self.parse_two)

    def parse_two(self, response):
        print("Parsing parse", self.form_dict)
        yield scrapy.FormRequest(
            self.form_url,
            formdata={
                '__EVENTTARGET': 'ddlexamtype',
                '__EVENTARGUMENT':'',
                '__LASTFOCUS': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                'ddlcollege':str(self.form_dict['collegecode']),
                'ddlexamtype':str(self.form_dict['examtype']),
                'ddlstream':'<-----Select----->',
                'txtrollno':'',
                'txtname':''
            },
            callback=self.parse_scheme
        )

    def parse_scheme(self, response):
        print("Parsing parse_scheme")
        yield scrapy.FormRequest(
            self.form_url,
            formdata={
                '__EVENTTARGET': 'ddlexamflag',
                '__EVENTARGUMENT':'',
                '__LASTFOCUS': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                'ddlcollege':str(self.form_dict['collegecode']),
                'ddlexamtype':str(self.form_dict['examtype']),
                'ddlexamflag':str(self.form_dict['examscheme']),
                'ddlstream':'<-----Select----->',
                'ddlpart':'<-----Select----->',
                'txtrollno':'',
                'txtname':''
            },
            callback=self.parse_stream
        )

    def parse_stream(self, response):
        print("Parsing parse_stream")
        yield scrapy.FormRequest(
            self.form_url,
            formdata={
                '__EVENTTARGET': 'ddlstream',
                '__EVENTARGUMENT':'',
                '__LASTFOCUS': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                'ddlcollege':str(self.form_dict['collegecode']),
                'ddlexamtype':str(self.form_dict['examtype']),
                'ddlexamflag':str(self.form_dict['examscheme']),
                'ddlstream':str(self.form_dict['streamcode']),
                'ddlpart':'<-----Select----->',
                'txtrollno':'',
                'txtname':''
            },
            callback=self.parse_course
        )

    def parse_course(self, response):
        print("Parsing parse_course")
        yield scrapy.FormRequest(
            self.form_url,
            formdata={
                '__EVENTTARGET': 'ddlcourse',
                '__EVENTARGUMENT':'',
                '__LASTFOCUS': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                'ddlcollege':str(self.form_dict['collegecode']),
                'ddlexamtype':str(self.form_dict['examtype']),
                'ddlexamflag':str(self.form_dict['examscheme']),
                'ddlstream':str(self.form_dict['streamcode']),
                'ddlcourse':str(self.form_dict['coursecode']),
                'ddlpart':'<-----Select----->',
                'txtrollno':'',
                'txtname':''
            },
            callback=self.parse_part
        )

    def parse_part(self, response):
        print("Parsing parse_part")
        yield scrapy.FormRequest(
            self.form_url,
            formdata={
                '__EVENTTARGET': 'ddlpart',
                '__EVENTARGUMENT':'',
                '__LASTFOCUS': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                'ddlcollege':str(self.form_dict['collegecode']),
                'ddlexamtype':str(self.form_dict['examtype']),
                'ddlexamflag':str(self.form_dict['examscheme']),
                'ddlstream':str(self.form_dict['streamcode']),
                'ddlcourse':str(self.form_dict['coursecode']),
                'ddlpart':str(self.form_dict['year']),
                'txtrollno':'',
                'txtname':''
            },
            callback=self.parse_submit
        )

    def parse_submit(self, response):
        user_data = self.new_list
        print("Parsing parse_submit")
        for d in user_data:
            yield scrapy.FormRequest(
                self.form_url,
                formdata={
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT':'',
                    '__LASTFOCUS': '',
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                    '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                    '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                    'ddlcollege':str(self.form_dict['collegecode']),
                    'ddlexamtype':str(self.form_dict['examtype']),
                    'ddlexamflag':str(self.form_dict['examscheme']),
                    'ddlstream':str(self.form_dict['streamcode']),
                    'ddlcourse':str(self.form_dict['coursecode']),
                    'ddlpart':str(self.form_dict['year']),
                    'ddlsem':str(self.form_dict['semester']),
                    'txtrollno':d[0],
                    'txtname':d[1],
                    'btnsearch':'Print Score Cart/Transcript'
                },
                callback=self.parse_results,
                meta={'name': d[1]}
            )

    def parse_results(self, response):

        with open('results.csv', 'a+') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            # mylist = response.css('#gvshow > tr > td::text').extract()
            new_list = []

            tr_list = []
            for l in response.css('#gvshow tr'):
                if l.css('td'):
                    td_list = []
                    for td in l.css('td'):
                        # print(td.css('::text').extract())
                        td_list.append(td.css('::text').extract_first())
                    tr_list += td_list

            item = response.meta.get('name')
            new_list.append(item)
            for ele in tr_list:
                if ele is not None:
                    if '/' in ele:
                        ele = ele.split('/')[0]
                    if '*' in ele:
                        ele = ele.split('*')[1]
                    new_list.append(ele)
                else:
                    new_list.append(ele)
            wr.writerow(new_list)


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(SpidyResults)
    process.start()
