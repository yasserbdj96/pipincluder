__version__='0.0.3'
__name__="pipincluder"
__author__="Yasser BDJ (Ro0t96)"
__author_email__="by.root96@gmail.com"
__description__="To import packages if they are found, or download them from pypi if they are not present.\nThis project is in order to bypass errors during importing any package."
__Author_WebSite__="https://byro0t96.github.io/"
__Source_Code__="https://github.com/byRo0t96/"+__name__
__keywords__=['python','pipincluder','import','from import','pip','pypi']
__install_requires__=['requests']
__license__='Apache Software License'
__copyright__='Copyright 2021 '+__author__

#__README_MD__:
__README_MD__title__="pipincluder for import packages without errors of unavailability."
__README_MD__description__=__description__
__README_MD__Installation__="pip install "+__name__
__README_MD__changelog__=['\n## 0.0.3\n- First public release.']

#__travis__:
__travis__install__=["pip3 install pipincluder || pip install pipincluder"]
__travis__script__=["python3 pipincluder/pipincluder.py || python pipincluder/pipincluder.py","python3 examples/example_1.py || python examples/example_1.py"]