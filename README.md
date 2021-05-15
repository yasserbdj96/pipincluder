
<h1>pipincluder for import packages without errors of unavailability.</h1>

<p>To import packages if they are found, or download them from pypi if they are not present.This project is in order to bypass errors during importing any package.</p>
<p align="center">
    <img align="center" src="https://travis-ci.com/byRo0t96/pipincluder.svg?branch=main">
    <img align="center" src="https://img.shields.io/github/issues/byRo0t96/pipincluder">
    <img align="center" src="https://img.shields.io/github/forks/byRo0t96/pipincluder">
    <img align="center" src="https://img.shields.io/github/stars/byRo0t96/pipincluder">
    <img align="center" src="https://img.shields.io/badge/license-Apache--2.0-green.svg">
    <img align="center" src="https://img.shields.io/badge/python-3.x.x-blue">
</p>
<h2>Installation:</h2>

```
pip install pipincluder==1.0.5
```

<h2>Usage:</h2>

```python
# USAGE :
#s
from pipincluder import pipincluder

exec(pipincluder(<YOUR_PACKAGES>).modules())
#e

```

<h2>Examples:</h2>

```python
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

```

<h2>Changelog:</h2>

```
## 1.0.5
 - fix bugs.
 - new build 

## 0.0.1
 - First public release.

```
<br>
<br>
<p align="center">
    <a align="center" href="https://byro0t96.github.io/">
        <img alt="byRo0t96" height="100" align="center" src="https://raw.githubusercontent.com/byRo0t96/byRo0t96/main/images/Ro0t-96_v.3.1.png">
    </a>
</p>

<p align="center">
    <a align="center" href="https://www.facebook.com/yasser.bdj.31">
        <img alt="facebook" align="center" src="https://img.shields.io/badge/Facebook-%2Fyasser.bdj.31-blue">
    </a>
	
   <a align="center" href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg">
        <img align="center"  alt="youtube" src="https://img.shields.io/badge/-YouTube-red">
    </a>
	
   <a href="https://www.linkedin.com/in/boudjada-yasser-a53543196" align="center" >
        <img align="center" alt="LinkedIn" src="https://img.shields.io/badge/-linkedin-blue">
    </a> 
    
   <a href="https://www.instagram.com/bdj.yasser/" align="center" >
        <img align="center" alt="instagram" src="https://img.shields.io/badge/instagram-%2Fbdj.yasser-orange">
    </a> 
        
   <a href="https://github.com/byRo0t96/" align="center" >
        <img align="center" alt="visitor-badge" src="https://visitor-badge.laobi.icu/badge?page_id=byRo0t96.byRo0t96">
    </a>
</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>