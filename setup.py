from setuptools import setup
from glob import glob
import os
current_path = os.path.dirname(os.path.realpath(__file__))

setup(
    name = 'uagents',
    version='1.2',
    packages=['uagents'],
    include_package_data=True,
    package_data = {"uagents": ["json/*.json"],"uagents": ["csv/*.csv"] }

)