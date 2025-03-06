from setuptools import find_packages, setup

package_name = 'delivery'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
    'setuptools',
    'rclpy',
    'std_msgs',  # Dépendance pour les messages standard
    'std_srvs',   # Dépendance pour le service Trigger
],
    zip_safe=True,
    maintainer='nouha',
    maintainer_email='nouha@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'suivi_livraison_node = delivery.suivi_livraison_node:main', 
            'commande_node = delivery.commande_node:main',
            'confirmation_livraison_node = delivery.confirmation_livraison_node:main', 
        ],
    },
)
