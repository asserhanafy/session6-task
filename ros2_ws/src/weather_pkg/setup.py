from setuptools import find_packages, setup

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asserhanafy',
    maintainer_email='asserhanafy68@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         'humidity_node = weather_pkg.humidity_node:main',
         'pressure_node = weather_pkg.pressure_node:main',
         'temperature_node = weather_pkg.temperature_node:main',
         'aggregator_node = weather_pkg.aggregator_node:main',
        ],
    },
)
