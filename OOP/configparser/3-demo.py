import configparser
config = configparser.ConfigParser()
config.read('example.ini')
config.add_section('test-add')

config.remove_section('bitbucket.org')
config.remove_option('topsecret.server.com',"forwardx11")


config.set('topsecret.server.com','k1','11111')
config.set('test-add','k2','22222')

config.write(open('new2.ini', "w"))
