

class init:
    def __init__(self):

        import checkUpdate
        import crawlerBasic
        import json
        import time
        import pickle
        import requests
        import os

        dateStamp = list(time.localtime(int(time.time())))
        date = str(dateStamp[0]) + str(dateStamp[1]) + str(dateStamp[2])
        with open('runTimeCache','r') as f:
            getIpTimeJson = json.loads(f.read())
            getIpTime = getIpTimeJson['getIp']

        crawlerBasic = crawlerBasic.crawlerComponent()

        # test WIFI connect
        try:
            requests.get('https://baidu.com',headers=crawlerBasic.get_crawel_header())
        except:
            print('[error] No wifi connect!')
            os._exit(0)

        # if not get IP
        if not getIpTime == date:
            print('[update] IpLib')
            # update ipLib
            crawlerBasic.updateIpLib()
            with open('ipCache.pkl','wb') as f:
                f.write(pickle.dumps(crawlerBasic.ipLib))

            # update runTime Cache
            with open('runTimeCache','w') as f:
                getIpTimeJson['getIp'] = date
                f.write(json.dumps(getIpTimeJson))

        else:
            with open('ipCache.pkl','rb') as f:
                ipLib = pickle.loads(f.read())
                crawlerBasic.setIpLib(ipLib)

        self.crawler = crawlerBasic

        # check update
        update = checkUpdate.update()
        if update.needUpdate():
            print('[check Update...]')
            update.update(crawlerBasic)
            if not update.isNewest():
                print('tool need update! ')
                print('+ New version: ' + update.update_c['update'])
                print('+ Your version: ' + update.origin_c['update'])
                print('+ Description: ' + update.update_c['desc'])
                input('enter to quit...')
                input()
                os._exit(0)
            else:
                print('[version] '+ update.origin_c['update'])

