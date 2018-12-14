from conans import ConanFile, MSBuild, tools, AutoToolsBuildEnvironment
from conans.tools import os_info

class FreeImageConan(ConanFile):
    name = "FreeImage"
    version = "3.18.0"
    license = "GNU"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/AnotherFoxGuy/conan-FreeImage"
    description = "FreeImage is an Open Source library project for developers who would like to support popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by today's multimedia applications."
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        tools.get("http://downloads.sourceforge.net/freeimage/FreeImage3180.zip")


    def build(self):
        with tools.chdir("./FreeImage"):
            if os_info.is_windows:
                msbuild = MSBuild(self)
                msbuild.build("FreeImage.2017.sln", platforms={"x86":"Win32"})
            else:
                autotools = AutoToolsBuildEnvironment(self)
                autotools.make()

    def package(self):
        self.copy("*.h", dst="include", src="FreeImage/Dist")
        self.copy("*.lib", dst="lib", src="FreeImage/Dist")
        self.copy("*.dll", dst="bin", src="FreeImage/Dist")
        self.copy("*.so", dst="lib", src="FreeImage/Dist")
        self.copy("*.a", dst="lib", src="FreeImage/Dist")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
