cmake_minimum_required(VERSION 3.15)

project(imgui)

add_library(${PROJECT_NAME})

target_sources(${PROJECT_NAME} PRIVATE
    imgui.cpp
    imgui_draw.cpp
    imgui_tables.cpp
    imgui_widgets.cpp   
)

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER 
"imgui.h;imgui_internal.h;imstb_textedit.h"
)

include(GNUInstallDirs)
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/dear-imgui/
)