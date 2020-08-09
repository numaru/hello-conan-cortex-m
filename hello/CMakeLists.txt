cmake_minimum_required(VERSION 3.15)

set(package_version 0.1.0)
project(Hello VERSION ${package_version} LANGUAGES C)

add_library(Hello
    src/hello/hello.c
)

target_include_directories(Hello
    PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
    PRIVATE
        src
)

target_compile_definitions(Hello
    PRIVATE
        GREETINGS=${HELLO_GREETINGS}
)

install(TARGETS Hello
    EXPORT HelloTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(EXPORT HelloTargets
    FILE HelloTargets.cmake
    NAMESPACE Hello::
    DESTINATION lib/cmake/Hello
)

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    HelloConfigVersion.cmake
    VERSION ${package_version}
    COMPATIBILITY SameMajorVersion
)

configure_file(HelloConfig.cmake.in HelloConfig.cmake @ONLY)

install(
    FILES
        ${CMAKE_CURRENT_BUILD_DIR}/HelloConfig.cmake
        ${CMAKE_CURRENT_BUILD_DIR}/HelloConfigVersion.cmake
    DESTINATION lib/cmake/Hello
)
