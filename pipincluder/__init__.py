#!/usr/bin/env python
# coding:utf-8
# Code by : Yasser BDJ
# E-mail  : yasser.bdj96@gmail.com
"""
#set:usage.py,examples.py,changelog.txt
##################################################################
# USAGE :
#s
from pipincluder import pipincluder

exec(pipincluder(<YOUR_PACKAGES>).modules())
#e
##################################################################
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
##################################################################
# CHANGELOG :
#s
## 1.0.6
 - fix bugs.

## 1.0.5
 - fix bugs.
 - new build 

## 0.0.1
 - First public release.
#e
##################################################################
"""
# VALUES :
__version__="1.0.6"
__name__="pipincluder"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="pipincluder for import packages without errors of unavailability."
__description__="To import packages if they are found, or download them from pypi if they are not present.This project is in order to bypass errors during importing any package."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=['']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
#s
import subprocess
import sys
import re
import requests

#start pipincluder class:
class pipincluder:
    def __init__(self,*package):
        self.package=package
    def modules(self):
        packages_works=[]
        for i in range(len(self.package)):
            try:
                exec(f"{self.package[i]}")
                packages_works.append(self.package[i])
            except ModuleNotFoundError:
                try:
                    result=re.search('from (.*) import',self.package[i])
                    if pipincluder.pipinstall(result.group(1))==True:
                        packages_works.append(self.package[i])
                except:
                    if self.package[i][:6]=="import":
                        result=re.search('import (.*)',self.package[i])
                        import_list=result.group(1).replace(" ","").split(',')
                        packages_works_2=[]
                        for j in range(len(import_list)):
                            if pipincluder.pipinstall(import_list[j])==True:
                                packages_works_2.append(import_list[j])
                        pp=""
                        for k in range(len(packages_works_2)):
                            if pp!="":
                                vrgl=","
                            else:
                                vrgl=""
                            pp=pp+vrgl+packages_works_2[k]
                        ok=f"import {pp}"
                        if ok!="import ":
                            packages_works.append()
        final=""
        for m in range(len(packages_works)):
            if final=="":
                br=""
            else:
                br="\n"
            final=final+br+packages_works[m]
        return final
    def pipinstall(pkg):
        try:
            exec(f"import {pkg}")
            return True
        except:
            response=requests.get(f"https://pypi.org/project/{pkg}")
            if response.status_code==200:
                subprocess.check_call([sys.executable,"-m","pip","install",pkg])
                return True
            else:
                return False
#e