import scrapy
import csv

class SpidyQuotesViewStateSpider(scrapy.Spider):
    name = 'spidyquotes-viewstate'
    form_url = 'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx'
    start_urls = [form_url]
    download_delay = 1.5

    def parse(self, response):
        print("Parsing parse")
        yield scrapy.FormRequest(
            'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx',
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
            'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx',
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
            'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx',
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
            'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx',
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
            'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx',
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
        user_data= [('17312911001', 'AASTHA SHRUTI'),('17312911002', 'ADIT NEGI'), ('17312911003', 'AKASH YADAV'), ('17312911004', 'ANAND RATNA RAWAT'), ('17312911005', 'ANKIT'), ('17312911006', 'ARJIT YADAV'), ('17312911007', 'ASHISH PRIYADARSHI'), ('17312911008', 'BALRAM MEENA'), ('17312911009', 'BHANU MITTAL'), ('17312911010', 'BHAWNA MAHARANA'), ('17312911011', 'DEVANSH GUPTA'), ('17312911012', 'DHAIRYA KATHPALIA'), ('17312911013', 'EKLAVYA CHOPRA'), ('17312911014', 'GAURAV'), ('17312911015', 'HARDIK KAPOOR'), ('17312911016', 'HARSHIT JOSHI'), ('17312911017', 'HITESH GAUTAM'), ('17312911018', 'KIRTI'), ('17312911019', 'MANAS AWASTHI'), ('17312911020', 'MANISH'), ('17312911021', 'MAYANK MALIK'), ('17312911022', 'NANCY'), ('17312911023', 'NAVEEN KUMAR'), ('17312911024', 'NIRUPAM GUNWAL'), ('17312911025', 'NITESH KUMAR'), ('17312911026', 'OMKAR CHAUDHARY'), ('17312911027', 'PARAS YADAV'), ('17312911028', 'PARTH GUPTA'), ('17312911029', 'PRABHAKAR DEEP TIRKEY'), ('17312911030', 'PRAKHAR AGARWAL'), ('17312911031', 'RAJ KUMAR SAH'), ('17312911032', 'RAVIKESH YADAV'), ('17312911033', 'RISHABH JAIN'), ('17312911034', 'RUDRANK RIYAM'), ('17312911035', 'SAHIL GUPTA'), ('17312911036', 'SAUMYA KUMARI'), ('17312911037', 'SHASHANK SINGH'), ('17312911038', 'SHARAD DUBEY'), ('17312911039', 'SHREYANSH TRIPATHI'), ('17312911040', 'SUNNY KOSTA'), ('17312911041', 'VEDANT BONDE'), ('17312911042', 'VIKASH VAIBHAV'), ('17312911043', 'YATHARTH RAI'), ('17312911044', 'ZALEESH AHMED')]
        # user_data=[('17312911016','HARSHIT'),('17312911017','HITESH')]
        print("Parsing parse_submit")
        for d in user_data:
            yield scrapy.FormRequest(
                'http://duexam1.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx',
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
                    'ddlsem':'I',
                    'txtrollno':d[0],
                    'txtname':d[1],
                    'btnsearch':'Print Score Cart/Transcript'
                },
                callback=self.parse_results,
                meta={'name': d[1]}
            )

    def parse_results(self, response):
        
        with open('harshit1.csv', 'a+') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            mylist = response.css('#gvshow > tr > td::text').extract()
            item = response.meta.get('name')
            mylist.append(item)
            wr.writerow(mylist)

            