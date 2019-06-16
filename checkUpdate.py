import time
import json
import requests

class update():
    def __init__(self):
        dateStamp = list(time.localtime(int(time.time())))
        self.date = str(dateStamp[0]) + str(dateStamp[1]) + str(dateStamp[2])
        with open('version','r') as f:
            self.origin_c = json.loads(f.read())

    def update(self,crawler):
        c = requests.get('https://gitlab.com/snippets/1866745/raw',
                         headers=crawler.get_crawel_header(),proxies=crawler.get_an_ip()).content.decode()
        self.update_c = json.loads(c)

    def isNewest(self):
        return self.update_c['update'] == self.origin_c['update']

    def needUpdate(self):
        return self.origin_c['checkUpdate']

