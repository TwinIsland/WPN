import init
import source.config as SSconfig
import random
import json
import writeGuiConfig
import vertify

print('initializing begin...')
init = init.init()
print('=====================\n')

crawler = init.crawler
GuiConfig = writeGuiConfig.gui_config()
ssAccount = SSconfig.getSS(crawler)
random.shuffle(ssAccount)

print('[OK] resource up to date')

with open('version','rb') as f:
    c = json.loads(f.read())
    isVer = c['checkUsable']
    checkDeep = c['checkDeep']

if checkDeep > len(ssAccount):
    checkDeep = len(ssAccount) - 1

validate = []
if isVer:
    print('[Begin] Verify Process with depth: ' + str(checkDeep))
    for index,ss in enumerate(ssAccount):

        if index >= checkDeep:
            break

        if vertify.check_ip_port(ss['server'],ss['server_port']):
            print('[Verify Pass] ' + ss['server'])
            GuiConfig.write(ss)
        else:
            print('[Verify Error] ' + ss['server'])
            continue
    print('[End] Verify Process')
print('[Save] All the change')
GuiConfig.saveChange()
print('[finish] All is Done, Enjoying!')
input('press to quit...')

