cmake_minimum_required(VERSION 2.6)



project (MOPSI)


add_executable (algoGenetique2 arbre.h arbre.cpp tools.h algogenetique.cpp algogenetique.h)



add_definitions(-DsrcPath="${CMAKE_CURRENT_SOURCE_DIR}")
