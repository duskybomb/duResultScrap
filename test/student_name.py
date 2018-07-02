# -*- coding: utf-8 -*-
import scrapy


class StudentNameSpider(scrapy.Spider):
    name = 'student_name'
    allowed_domains = ['du.ac.in']
    start_urls = ['http://duexam2.du.ac.in/RSLT_MJ2018/Students/List_Of_Students.aspx?StdType=REG&ExamFlag=UG_SEMESTER_4Y&CourseCode=911&CourseName=(C.I.C)%20-%20B.Tech%20(Information%20Technology%20and%20Mathematical%20Innovations)&Part=I&Sem=II']

    def parse(self, response):
        resp_list = response.css('#gvshow > tr > td::text').extract()
        print(resp_list)
