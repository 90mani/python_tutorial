from jproperties import Properties

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)
#print(configs.get("host"))
print(configs.get("DB_User"))  
# PropertyTuple(data='root', meta={})

print(f'Database User: {configs.get("DB_User").data}')  
# Database User: root

print(f'Database Password: {configs["DB_PWD"].data}')  
# Database Password: root@neon