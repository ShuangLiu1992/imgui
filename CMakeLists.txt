cmake_minimum_required(VERSION 3.15)

project(imgui)

add_library(${PROJECT_NAME})

target_sources(${PROJECT_NAME} PRIVATE
    imgui.cpp
    imgui_draw.cpp
    imgui_tables.cpp
    imgui_widgets.cpp   
)
target_compile_definitions(${PROJECT_NAME} PUBLIC "-DIMGUI_USER_CONFIG=\"im_user_config.h\"")

option(ENABLE_TESTING "Enable test engine." OFF)
set(public_headers 
    imconfig.h 
    imgui.h
    imgui_internal.h
    imstb_textedit.h
    im_user_config.h
)
if (ENABLE_TESTING)
    target_sources(${PROJECT_NAME} PRIVATE
        imgui_test_engine/imgui_test_engine/imgui_capture_tool.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_context.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_coroutine.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_engine.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_exporters.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_perftool.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_ui.cpp
        imgui_test_engine/imgui_test_engine/imgui_te_utils.cpp
    )
    list(APPEND public_headers 
        imgui_test_engine/imgui_test_engine/imgui_te_engine.h
        imgui_test_engine/imgui_test_engine/imgui_te_ui.h
        imgui_test_engine/imgui_test_engine/imgui_capture_tool.h
        imgui_test_engine/imgui_test_engine/imgui_te_coroutine.h
        imgui_test_engine/imgui_test_engine/imgui_te_context.h
        imgui_test_engine/imgui_test_engine/imgui_te_exporters.h
        imgui_test_engine/imgui_test_engine/imgui_te_imconfig.h
        imgui_test_engine/imgui_test_engine/imgui_te_internal.h
        imgui_test_engine/imgui_test_engine/imgui_te_perftool.h
        imgui_test_engine/imgui_test_engine/imgui_te_utils.h
    )
    target_compile_definitions(${PROJECT_NAME} PUBLIC -DENABLE_TESTING=1)
    target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
    target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/imgui_test_engine/imgui_test_engine/)
endif()

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "${public_headers}")

include(GNUInstallDirs)
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/dear-imgui/
)