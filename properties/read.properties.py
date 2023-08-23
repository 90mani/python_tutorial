from jproperties import Properties

configs = Properties()
with open(
    "C:/Users/Home/Documents/workpython/python_tutorial/properties/database.properties.py.", 'rb'
    )as config_file:
    configs.load(config_file)

print(configs.get("mydbhost"))
print(configs.get("username"))
print(configs.get("password"))  


