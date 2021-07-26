from setuptools import setup,find_packages
setup(
    name="pipincluder",
    version="1.0.6",
    author="Yasser Bdj (Boudjada Yasser)",
    author_email="yasser.bdj96@gmail.com",
    description='''To import packages if they are found, or download them from pypi if they are not present.This project is in order to bypass errors during importing any package.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    url="https://github.com/yasserbdj96/pipincluder",
    project_urls={
        'Author WebSite': "https://yasserbdj96.github.io/",
    },
    install_requires=[''],
    keywords=['yasserbdj96', 'python', 'pipincluder', 'for', 'import', 'packages', 'without', 'errors', 'of', 'unavailability.', 'To', 'import', 'packages', 'if', 'they', 'are', 'found,', 'or', 'download', 'them', 'from', 'pypi', 'if', 'they', 'are', 'not', 'present.This', 'project', 'is', 'in', 'order', 'to', 'bypass', 'errors', 'during', 'importing', 'any', 'package.'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Communications :: Email'
    ],
    python_requires=">=3.x.x"
)