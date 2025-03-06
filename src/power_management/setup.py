from setuptools import setup

package_name = 'power_management'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'std_msgs', 'sensor_msgs'],
    zip_safe=True,
    maintainer='hafsa el kasmi',
    maintainer_email='elkasmihafsa28@gmail.com',
    description="Un package pour la gestion de l'alimentation du drone",
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_monitor = power_management.battery_monitor:main',
            'emergency_handler = power_management.emergency_handler:main',
            'return_to_base_server = power_management.return_to_base_server:main',
        ],
    },
)

