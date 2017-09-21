cmake_minimum_required(VERSION 3.5)

if(NOT ${WIN32})
    message("AcceleratedVision doesn't support Linux now+.")
else()
    message("AcceleratedVision merely supports Windows now, but will support linux in the future.")
    set(PROJECT_NAME "SimpleMath")
    project(${PROJECT_NAME})
    include_directories(${${PROJECT_NAME}_SOURCE_DIR}/include)
    aux_source_directory(${${PROJECT_NAME}_SOURCE_DIR}/sources DIR_SRCS)
    add_library(simplemath SHARED ${DIR_SRCS}) # generate dll
endif()