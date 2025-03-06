
from setuptools import find_packages, setup

package_name = 'navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         ('share/navigation/srv', ['srv/PlanPath.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aicha',
    maintainer_email='aicha@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_generator_node_withoutSrv = navigation.path_generator_node_withoutSrv:main',
            'obstacle_avoider_node = navigation.obstacle_avoider_node:main',
            'path_generator_node = navigation.path_generator_node:main',
            ]
    },
)
