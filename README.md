
<h1>pipincluder for import packages without errors of unavailability.</h1>

<p>To import packages if they are found, or download them from pypi if they are not present.This project is in order to bypass errors during importing any package.</p>

<h2>Installation:</h2>

```
pip install pipincluder==1.0.6
```

<h2>Usage:</h2>

```python
from pipincluder import pipincluder
exec(pipincluder(<YOUR_PACKAGES>).modules())

```

<h2>Examples:</h2>

```python
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

```

<h2>Changelog:</h2>

```
## 1.0.6
 - fix bugs.
## 1.0.5
 - fix bugs.
 - new build 
## 0.0.1
 - First public release.

```

<h1></h1> 
   
<p align="center">
   <a href="https://www.linkedin.com/in/yasserbdj96" align="center"><img align="center" alt="linkedin" src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white"></a>
   <a href="https://yasserbdj96.github.io" align="center"><img align="center" alt="website" src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white"></a>
   <a href="https://twitter.com/yasserbdj96" align="center"><img align="center" alt="twitter" src="https://img.shields.io/badge/-Twitter-00acee?style=flat-square&logo=Twitter&logoColor=white"></a>
   <a href="https://www.instagram.com/yasserbdj96" align="center"><img align="center" alt="instagram" src="https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white"></a>
   <a href="https://www.facebook.com/yasserbdj96" align="center"><img align="center" alt="facebook" src="https://img.shields.io/badge/-facebook-0088cc?style=flat-square&logo=facebook&logoColor=white"></a>
   <a href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg" align="center"><img align="center" alt="youtube" src="https://img.shields.io/badge/-youtube-ea4335?style=flat-square&logo=youtube&logoColor=white"></a>
   <a href="https://pypi.org/user/yasserbdj96" align="center"><img align="center" alt="pypi" src="https://img.shields.io/badge/-pypi-efeeea?style=flat-square&logo=pypi"></a>
</p>

<p align="center">
    BTC : 16mUJYXdNh9VkjN3MQawA8wvYJqL9F5CKZ

</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>

<div align="center">
    <a href="https://yasserbdj96.github.io"><img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/yasserbdj96/main/images/yasserbdj96.png"></a>
   <br>
    <a href="https://github.com/yasserbdj96/" align="center"><img align="center" alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.pipincluder"></a>
</div>
