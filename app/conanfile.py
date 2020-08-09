from conans import ConanFile, CMake

class AppConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Hello/0.1.0@kin/testing", "Lm3s6965Hal/0.1.0@kin/testing", 
    generators = "cmake_paths"
    default_options = {"Hello:greetings": "Hello World!"}

    def build(self):
        args = [
            "-DCMAKE_TOOLCHAIN_FILE=conan_paths.cmake"
        ]
        cmake = CMake(self)
        cmake.configure(args)
        cmake.build()