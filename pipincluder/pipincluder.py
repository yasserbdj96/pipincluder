#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
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