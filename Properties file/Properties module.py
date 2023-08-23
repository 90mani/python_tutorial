from jproperties import Properties

configs=Properties()
with open(
    "C:\\Users\\ACER\\Pictures\\python code\\python_tutorial\\Properties file\\local_host.properties","rb"
    ,)as config_file:
         configs.load(config_file)

print(configs.get("myname")) 
print(configs.get("host"))
print(configs.get("user"))
