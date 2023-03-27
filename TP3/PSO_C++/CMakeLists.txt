cmake_minimum_required(VERSION 3.22)
project(PSO_C__)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(PSO_C__
        optim.cpp
        optim.h
        particle.cpp
        particle.h
        pso.cpp)
