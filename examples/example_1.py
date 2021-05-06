#s
from pipincluder import pipincluder

# Example:1
p1=pipincluder("from os import path",
               "import kkkk,llll ,mmmmm,hahahahahaha",
               "from ashar import ashar")
exec(p1.modules())

#test ashar package:
print(ashar("123","this is just an example :)").encode())
#e