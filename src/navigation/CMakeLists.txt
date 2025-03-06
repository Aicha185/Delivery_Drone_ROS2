cmake_minimum_required(VERSION 3.5)
project(navigation)

# Trouver les dépendances nécessaires
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Générer les interfaces à partir du fichier .srv
rosidl_generate_interfaces(${PROJECT_NAME} "srv/PlanPath.srv")

# Installer les fichiers Python
ament_python_install_package(${PROJECT_NAME})

# Installer les fichiers de messages et services
install(
  DIRECTORY srv
  DESTINATION share/${PROJECT_NAME}
)
install(
  DIRECTORY launch worlds urdf
  DESTINATION share/${PROJECT_NAME}
)

# Installer les scripts Python
install(
  PROGRAMS
    src/path_generator_node.py  # Chemin vers votre script Python
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()