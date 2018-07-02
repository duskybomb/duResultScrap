import scrapy
import csv


class SpidyQuotesViewStateSpider(scrapy.Spider):
    name = 'results'
    form_url = 'http://duexam2.du.ac.in/RSLT_MJ2018/Students/Combine_GradeCard.aspx'
    start_urls = ['http://duexam2.du.ac.in/RSLT_MJ2018/Students/List_Of_Students.aspx?StdType=REG&ExamFlag=UG_SEMESTER_4Y&CourseCode=911&CourseName=(C.I.C)%20-%20B.Tech%20(Information%20Technology%20and%20Mathematical%20Innovations)&Part=I&Sem=II']
    download_delay = 1.5

    def parse(self, response):
        resp_list = response.css('#gvshow > tr > td::text').extract()
        self.new_list = []
        i = 0
        while i < len(resp_list):
            if i == 0:
                pass
            elif i % 2 == 1:
                new_sub_list = [resp_list[i]]
            elif i % 2 == 0:
                new_sub_list.append(resp_list[i])
                self.new_list.append(new_sub_list)
                i = i + 2
            i += 1
        print(self.new_list)
        yield response.follow(self.form_url, self.parse_two)

    def parse_two(self, response):
        print("Parsing parse")
        yield scrapy.FormRequest(
            self.form_url,
            formdata={
                '__EVENTTARGET': 'ddlexamtype',
                '__EVENTARGUMENT':'',
                '__LASTFOCUS': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                '__VIEWSTATEGENERATOR': response.css('input#__VIEWSTATEGENERATOR::attr(value)').extract_first(),
                '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                'ddlcollege':'312',
                'ddlexamtype':'Semester',
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
                'ddlcollege':'312',
                'ddlexamtype':'Semester',
                'ddlexamflag':'UG_SEMESTER_4Y',
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
                'ddlcollege':'312',
                'ddlexamtype':'Semester',
                'ddlexamflag':'UG_SEMESTER_4Y',
                'ddlstream':'SC',
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
                'ddlcollege':'312',
                'ddlexamtype':'Semester',
                'ddlexamflag':'UG_SEMESTER_4Y',
                'ddlstream':'SC',
                'ddlcourse':'911',
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
                'ddlcollege':'312',
                'ddlexamtype':'Semester',
                'ddlexamflag':'UG_SEMESTER_4Y',
                'ddlstream':'SC',
                'ddlcourse':'911',
                'ddlpart':'I',
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
                    'ddlcollege':'312',
                    'ddlexamtype':'Semester',
                    'ddlexamflag':'UG_SEMESTER_4Y',
                    'ddlstream':'SC',
                    'ddlcourse':'911',
                    'ddlpart':'I',
                    'ddlsem':'II',
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
            mylist = response.css('#gvshow > tr > td::text').extract()
            new_list = []
            item = response.meta.get('name')
            new_list.append(item)
            for ele in mylist:
                new_list.append(ele.split('/')[0])
            wr.writerow(new_list)
