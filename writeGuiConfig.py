import json

class gui_config:
    def __init__(self):
        with open('ss/gui-config.json','rb') as f:
            self.origin = json.loads(f.read())
            self.configs = self.origin['configs']

    def write(self,config):
        # {server,server_port,password,method}

        #{'server':, 'server_port': , 'password': '', 'method': '', 'plugin': 'null', 'plugin_opts': 'null', 'plugin_args': 'null',
        # 'remarks': 'null', 'timeout': 5}

        config['plugin'] = ''
        config['plugin_opts'] = ''
        config['plugin_args'] = ''
        config['remarks'] = ''
        config['timeout'] = 5

        self.configs.append(config)

    def saveChange(self):
        self.origin['configs'] = self.configs

        with open('ss/gui-config.json', 'w') as f:
            f.write(json.dumps(self.origin))
