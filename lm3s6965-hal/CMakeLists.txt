cmake_minimum_required(VERSION 3.15)

set(package_version 0.1.0)
project(Lm3s6965Hal VERSION ${package_version} LANGUAGES C ASM)

add_library(Lm3s6965HalWeak
    src/system_lm3s.c
    $<$<STREQUAL:${CMAKE_C_COMPILER_ID},GNU>:src/GNU/startup_lm3s6965.S>
    src/embedded-hal/delay.c
    src/embedded-hal/console.c
)

target_include_directories(Lm3s6965HalWeak
    PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
    PRIVATE
        src
)

target_link_options(Lm3s6965HalWeak
    INTERFACE
        $<$<STREQUAL:${CMAKE_C_COMPILER_ID},GNU>:-T ${CMAKE_CURRENT_SOURCE_DIR}/src/GNU/lm3s6965.ld>
)

add_library(Lm3s6965Hal INTERFACE)

target_link_libraries(Lm3s6965Hal
    INTERFACE
        $<$<STREQUAL:${CMAKE_C_COMPILER_ID},GNU>:-Wl,-whole-archive>
            Lm3s6965HalWeak
        $<$<STREQUAL:${CMAKE_C_COMPILER_ID},GNU>:-Wl,-no-whole-archive>
)

install(TARGETS
        Lm3s6965HalWeak
        Lm3s6965Hal
    EXPORT Lm3s6965HalTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(EXPORT Lm3s6965HalTargets
    FILE Lm3s6965HalTargets.cmake
    NAMESPACE Lm3s6965Hal::
    DESTINATION lib/cmake/Lm3s6965Hal
)

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    Lm3s6965HalConfigVersion.cmake
    VERSION ${package_version}
    COMPATIBILITY SameMajorVersion
)

configure_file(Lm3s6965HalConfig.cmake.in Lm3s6965HalConfig.cmake @ONLY)

install(
    FILES
        ${CMAKE_CURRENT_BUILD_DIR}/Lm3s6965HalConfig.cmake
        ${CMAKE_CURRENT_BUILD_DIR}/Lm3s6965HalConfigVersion.cmake
    DESTINATION lib/cmake/Lm3s6965Hal
)
