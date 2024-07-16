cmake_minimum_required(VERSION 2.8.3)
project(vision_and_object_recognition)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

## Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a catkin package
catkin_package()

## Mark executables and/or libraries for installation
catkin_install_python(PROGRAMS
  scripts/obj_recogn.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark other files for installation (e.g. launch files)
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

message("CMakeLists.txt for vision_and_object_recognition configured")
message("Script to install: ${CMAKE_CURRENT_SOURCE_DIR}/scripts/obj_recogn.py")

