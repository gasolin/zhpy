from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
from pkg_resources import DistributionNotFound

install_requires = ["zhpy>=0.9"]

setup(
    name="zh_module_name",
    version=0.1,
    author="gasolin",
    author_email="gasolin+zhpy@gmail.com",
    license="MIT",
    keywords = "traditional, simplified, chinese",
    description="module plugin for zhpy",
    long_description="""sample module plugin for zhpy
    """,
    url="http://code.google.com/p/zhpy",
    zip_safe=False,
    install_requires = install_requires,
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup"]),
    entry_points = """
    [zhpy.twdict]
    tw_module_name = word:tw_dict
    [zhpy.cndict]
    cn_module_name = word:cn_dict
    """,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )