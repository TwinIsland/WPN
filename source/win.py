import requests
import lxml.etree

def getSS(crawler):
    api = 'https://www.youneed.win/free-ss'

    c = lxml.etree.HTML(requests.get(api,headers=crawler.get_crawel_header(),proxies=crawler.get_an_ip()).content)
    r = []
    count = 0

    while True:
        count += 1
        # //*[@id="post-box"]/div/section/table/tbody/tr[1]/td[1]

        xpathIP = '//*[@id="post-box"]/div/section/table/tbody/tr[' + str(count) + ']/td[1]/text()'
        xpathPort = '//*[@id="post-box"]/div/section/table/tbody/tr[' + str(count) + ']/td[2]/text()'
        xpathPass = '//*[@id="post-box"]/div/section/table/tbody/tr[' + str(count) + ']/td[3]/text()'
        xpathEnc = '//*[@id="post-box"]/div/section/table/tbody/tr[' + str(count) + ']/td[4]/text()'
        #xpathPlace = '//*[@id="post-box"]/div/section/table/tbody/tr[' + str(count) + ']/td[6]'

        ip = c.xpath(xpathIP)

        if ip == []:
            break
        r.append({'server':ip[0],'server_port':c.xpath(xpathPort)[0],'password':c.xpath(xpathPass)[0],'method':c.xpath(xpathEnc)[0]})

    return r
