from jproperties import Properties

configs=Properties()
with open(
    "E:\\python code\\python_tutorial\\properties\\database-example.properties","rb",)as config_file:
         configs.load(config_file)

print(configs.get("password")) 
print(configs.get("host"))
print(configs.get("user"))