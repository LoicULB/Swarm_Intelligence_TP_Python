cmake_minimum_required(VERSION 3.22)
project(aco_implemented)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_executable(aco_implemented
        src/aco.cpp
        src/ant.cpp
        src/ant.h
        src/tsp.cpp
        src/tsp.h)
