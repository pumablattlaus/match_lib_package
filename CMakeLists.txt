cmake_minimum_required(VERSION 3.0.2)
project(match_lib_package)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

include_directories()

# install(PROGRAMS
#   # Optional: add executable scripts here
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )
catkin_install_python(PROGRAMS
  # nodes/force_watchdog.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
