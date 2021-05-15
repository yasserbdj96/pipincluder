#!/usr/bin/env python
# coding:utf-8
"""
#set:usage,examples,changelog
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
"""
# VALUES :
#s
__version__="1.0.5"
__name__="pipincluder"
__author__="Yasser BDJ (Ro0t96)"
__author_email__="by.root96@gmail.com"
__title__="pipincluder for import packages without errors of unavailability."
__description__="To import packages if they are found, or download them from pypi if they are not present.This project is in order to bypass errors during importing any package."
__author_website__="https://byro0t96.github.io/"
__source_code__=f"https://github.com/byRo0t96/{__name__}"
__keywords__=['python','pip','install']
__install_requires__=['requests']
__Installation__="pip install "+__name__+"=="+__version__
__license__='Apache Software License'
__license_text__=f'''Copyright (c) 2008->Present, {__author__}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
__copyright__='Copyright 2008 -> Present, '+__author__
__changelog__=("## 1.0.5\n - fix bugs.\n - new build \n\n")
__changelog__=__changelog__+"## 0.0.1\n - First public release.\n"

__github_user_name__="byRo0t96"
##################################################################
#e

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