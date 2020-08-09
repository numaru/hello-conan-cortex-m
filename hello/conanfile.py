from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"greetings": "ANY"}
    default_options = {"greetings": "Hello World!"}
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        args = []
        greetings = self.options.get_safe("greetings")
        if greetings:
            args.append('-DHELLO_GREETINGS="{}"'.format(greetings))
        cmake.configure(args)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="inc")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*HelloTargets.cmake", dst="lib/cmake/Hello", keep_path=False)
        self.copy("*HelloTargets-*.cmake", dst="lib/cmake/Hello", keep_path=False)
        self.copy("*HelloConfig.cmake", dst="lib/cmake/Hello", keep_path=False)
        self.copy("*HelloConfigVersion.cmake", dst="lib/cmake/Hello", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
