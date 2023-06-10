#pragma once
#define IMGUI_DEFINE_MATH_OPERATORS
#define ImDrawIdx unsigned int
#if ENABLE_TESTING
#define IMGUI_TEST_ENGINE_ENABLE_COROUTINE_STDTHREAD_IMPL 1
#include "imgui_te_imconfig.h"
#endif