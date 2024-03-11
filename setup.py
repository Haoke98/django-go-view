# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/3/12
@Software: PyCharm
@disc:
======================================="""
"""
The build/compilations setup
>> pip install -r requirements.txt
>> python setup.py install
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    packages=["goview"],
    package_data={'goview': ['frontend/*']},
    entry_points={
        'console_scripts': [

        ],
    },
)