from setuptools import setup, find_packages

print(find_packages())
setup(
name='ml_yara_generator',
version='0.1.0',
author='Yohann Sillam',
author_email='yohannsillam@gmail.com',
packages= find_packages(),
package_dir={"main":"ml_yara_generator"},
url='https://github.com/ysillam/ml_yara_generator',
license='LICENSE.txt',
description=' This projects gives ability to automatically generate yara rules based on ML analysis of malicious samples. ',
long_description=open('README.md').read(),
install_requires=[
   "sklearn",
   "pandas"
],
)