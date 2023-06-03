from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, CMakeToolchain


class IMGUIConan(ConanFile):
    name = "imgui"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "ImDrawIdx": ["unsigned int", "unsigned short"]
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "ImDrawIdx": "unsigned int"
    }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = 1
        tc.presets_prefix = f"{self.settings.os}_{self.settings.build_type}_{self.settings.arch}"
        tc.generate()

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "imgui")
        self.cpp_info.includedirs = ["include", "include/dear-imgui"]
        self.cpp_info.libs = conan.tools.files.collect_libs(self)
