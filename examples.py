# EXAMPLES :
#s
try:
    from pipincluder import pipincluder
except:
    print("please use this command : pip install pipincluder")
    exit()

# Example:1
exec(pipincluder("from os import path",
                 "from hexor import hexor",
                 "from ashar import ashar").modules())
#test ashar package:
print(ashar("123","this is just an example :)").encode())
#e
