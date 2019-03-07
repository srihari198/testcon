from conans import ConanFile, CMake

class Pkg(ConanFile):
    name = "TestA"
    version = "1.0.0"
    settings = "os", "compiler", "arch", "build_type"
    requires = "TestB/1.0.0@user/testing"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["helloA"]
