from setuptools import setup, find_packages

setup(
    name ='mypack',
    version='0,1',
    packages=find_packages(exclude =['test*']),
    license='MIT',
    description='EDSA example pytgon package',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<Your Name>',
    author_email='<Your Email>'
)