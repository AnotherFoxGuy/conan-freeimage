from conans import ConanFile, MSBuild, tools, AutoToolsBuildEnvironment
from conans.tools import os_info


class freeimageConan(ConanFile):
    name = "freeimage"
    version = "3.18.0"
    license = "GNU"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/AnotherFoxGuy/conan-freeimage"
    description = "FreeImage is an Open Source library project for developers who would like to support popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by today's multimedia applications."
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        tools.get("http://downloads.sourceforge.net/freeimage/FreeImage3180.zip")

    def build(self):
        with tools.chdir("./FreeImage"):
            if os_info.is_windows:
                msbuild = MSBuild(self)
                msbuild.build("FreeImage.2017.sln", platforms={"x86": "Win32"})
            else:
                autotools = AutoToolsBuildEnvironment(self)
                autotools.make()

    def package(self):
        self.copy("*.h", dst="include", src="FreeImage/Dist", keep_path=False)
        self.copy("*.lib", dst="lib", src="FreeImage/Dist", keep_path=False)
        self.copy("*.dll", dst="bin", src="FreeImage/Dist", keep_path=False)
        self.copy("*.so", dst="lib", src="FreeImage/Dist", keep_path=False)
        self.copy("*.a", dst="lib", src="FreeImage/Dist", keep_path=False)
        self.copy("*.lib", dst="lib", src="FreeImage/Source", keep_path=False)
        self.copy("*.dll", dst="bin", src="FreeImage/Source", keep_path=False)
        self.copy("*.so", dst="lib", src="FreeImage/Source", keep_path=False)
        self.copy("*.a", dst="lib", src="FreeImage/Source", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
