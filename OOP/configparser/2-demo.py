import configparser
config = configparser.ConfigParser()
#print(config.sections())
config.read('example.ini')
#print(config.sections())
#['bitbucket.org', 'topsecret.server.com', 'hello'] 主配置段
#print('hello' in config) #true 说明是否存在
#print(config['hello']["jesse"]) #123456 打印出具体的配置信息


#print(config['hello'])          #hello>
#<Section: hello>
#for key in config['hello']:     # 注意,有default会默认default的键
#    print(key)
#jesse
#feiyu

print(config.options('hello'))  # 同for循环,找到'bitbucket.org'下所有键

print(config.items('hello'))    #找到'bitbucket.org'下所有键值对

print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value
