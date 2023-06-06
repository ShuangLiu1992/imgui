from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, CMakeToolchain
import os

class IMGUIConan(ConanFile):
    name = "imgui"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "enable_testing": [True, False],
        "ImDrawIdx": ["unsigned int", "unsigned short"]
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "enable_testing": True,
        "ImDrawIdx": "unsigned int"
    }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = 1
        tc.variables["ENABLE_TESTING"] = self.options.enable_testing
        tc.presets_prefix = f"{self.settings.os}_{self.settings.build_type}_{self.settings.arch}"
        if self.settings.os == "Emscripten" and self.options.enable_testing:
            tc.preprocessor_definitions["_X86_"] = 1
        tc.generate()

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)
        conan.tools.files.copy(self, "*", os.path.join(self.recipe_folder, "..", "imgui_test_engine"), os.path.join(self.export_sources_folder, "imgui_test_engine"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "imgui")
        self.cpp_info.includedirs = ["include", "include/dear-imgui"]
        self.cpp_info.libs = conan.tools.files.collect_libs(self)
        self.cpp_info.defines = ["IMGUI_USER_CONFIG=\"im_user_config.h\""]
