from setuptools import setup,find_packages
setup(
    name="pipincluder",
    version="1.0.5",
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='''To import packages if they are found, or download them from pypi if they are not present.This project is in order to bypass errors during importing any package.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license="Apache Software License",
    packages=find_packages(),
    project_urls={
        'Author WebSite': "https://byro0t96.github.io/",
        'Source Code': "https://github.com/byRo0t96/pipincluder",
    },
    install_requires=['requests'],
    keywords=['python', 'pip', 'install'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.x.x"
)