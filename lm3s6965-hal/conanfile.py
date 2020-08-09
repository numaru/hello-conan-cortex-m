from conans import ConanFile, CMake, tools


class Lm3s6965HalConan(ConanFile):
    name = "Lm3s6965Hal"
    version = "0.1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Lm3s6965Hal here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="inc")
        self.copy("*Lm3s6965Hal.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy(
            "*Lm3s6965HalTargets.cmake", dst="lib/cmake/Lm3s6965Hal", keep_path=False
        )
        self.copy(
            "*Lm3s6965HalTargets-*.cmake", dst="lib/cmake/Lm3s6965Hal", keep_path=False
        )
        self.copy(
            "*Lm3s6965HalConfig.cmake", dst="lib/cmake/Lm3s6965Hal", keep_path=False
        )
        self.copy(
            "*Lm3s6965HalConfigVersion.cmake",
            dst="lib/cmake/Lm3s6965Hal",
            keep_path=False,
        )

    def package_info(self):
        self.cpp_info.libs = ["Lm3s6965Hal"]
