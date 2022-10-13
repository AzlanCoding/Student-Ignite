# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\Student-Ignite_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Student-Ignite_autogen.dir\\ParseCache.txt"
  "Student-Ignite_autogen"
  )
endif()
