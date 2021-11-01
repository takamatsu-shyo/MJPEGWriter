cmake_minimum_required(VERSION 3.10)

# set the project name
project(_MJPEGWriter)

set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)

add_library(. MJPEGWriter.cpp)

include_directories(
    ${OpenCV_INCLUDE_DIRS}
)


add_executable(_MJPEGWriter main.cpp MJPEGWriter.cpp)

target_link_libraries(
    _MJPEGWriter
    ${OpenCV_LIBS}
    Threads::Threads
)

