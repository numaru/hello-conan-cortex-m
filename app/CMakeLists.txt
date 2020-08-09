cmake_minimum_required(VERSION 3.15)

project(App VERSION 0.1.0 LANGUAGES C)

add_executable(App
    src/app/main.c
)

target_include_directories(App
    PUBLIC
        inc
    PRIVATE
        src
)

find_package(Hello)
find_package(Lm3s6965Hal)

target_link_libraries(App
    PUBLIC
        Hello::Hello
        Lm3s6965Hal::Lm3s6965Hal
)
