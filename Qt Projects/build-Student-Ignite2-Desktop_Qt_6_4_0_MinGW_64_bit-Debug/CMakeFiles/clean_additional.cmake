# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\appStudent-Ignite2_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\appStudent-Ignite2_autogen.dir\\ParseCache.txt"
  "appStudent-Ignite2_autogen"
  )
endif()
