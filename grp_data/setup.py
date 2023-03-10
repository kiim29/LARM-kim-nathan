import os
from glob import glob
from setuptools import setup

package_name = 'grp_data'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bot',
    maintainer_email='bot@mb6.imt-nord-europe.fr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scan_echo = grp_data.scan_echo:main',
            'reactive_move = grp_data.reactive_move:main',
            'realsense = grp_data.realsense:process_img',
            'bottles_detect = grp_data.bottles_detect:main',
            'marker = grp_data.marker:main'
        ],
    },
)
