import os
import sys
from glob import glob
from setuptools import setup

package_name = 'cnc_interface'
py_version = ".".join(map(str, sys.version_info[:2]))
site_pkgs_path = 'lib/python' + py_version + '/site-packages/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
            site_pkgs_path + '/static/dist',
            glob(package_name + '/static/dist/*.*')
        ),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kai',
    maintainer_email='lkw303@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cnc_interface_node=cnc_interface.cnc_interface:main'
        ],
    },
)
