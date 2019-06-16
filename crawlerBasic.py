'''

Introduction:

This project was a part of Gargantua Project
and use to build a free and public book resources
database


Fot this program:

It contain some basic manipulation of Database and crawler

'''

from lxml import etree
import requests as rq
import random


class crawlerComponent:

    def updateIpLib(self):
        '''

        initialize crawler with ipLib
        [ip, type, port]

        '''
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}


        ipLib = []
        url = 'https://www.xicidaili.com/nn/'
        r = etree.HTML(rq.get(url, headers=header).content)
        # //*[@id="ip_list"]/tr[2]/td[2]
        # //*[@id="ip_list"]/tr[3]/td[2]
        # //*[@id="ip_list"]/tr[101]/td[2]
        for i in range(2, 101):
            ip = r.xpath('//*[@id="ip_list"]/tr[' + str(i) + ']/td[2]/text()')[0]
            type = r.xpath('//*[@id="ip_list"]/tr[' + str(i) + ']/td[6]/text()')[0]
            port = r.xpath('//*[@id="ip_list"]/tr[' + str(i) + ']/td[3]/text()')[0]
            ipLib.append([ip, type, port])

        self.ipLib = ipLib


    def setIpLib(self,ipLib):
        self.ipLib = ipLib

    def get_crawel_header(self):
        '''

        :return: header
        :return type: dict

        '''
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

        return header


    def get_an_ip(self):
        '''

        :param ipLib:
        :return: an random ip which can directly used by 'proxies'

        '''
        if self.ipLib == []:
            return {}
        choice = random.choice(self.ipLib)
        return {choice[1]: choice[0] + ':' + choice[2]}
