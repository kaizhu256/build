# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.0

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer

# Include any dependencies generated for this target.
include CMakeFiles/optimizer.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/optimizer.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/optimizer.dir/flags.make

CMakeFiles/optimizer.dir/parser.cpp.o: CMakeFiles/optimizer.dir/flags.make
CMakeFiles/optimizer.dir/parser.cpp.o: /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/parser.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/optimizer.dir/parser.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/optimizer.dir/parser.cpp.o -c /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/parser.cpp

CMakeFiles/optimizer.dir/parser.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/optimizer.dir/parser.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/parser.cpp > CMakeFiles/optimizer.dir/parser.cpp.i

CMakeFiles/optimizer.dir/parser.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/optimizer.dir/parser.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/parser.cpp -o CMakeFiles/optimizer.dir/parser.cpp.s

CMakeFiles/optimizer.dir/parser.cpp.o.requires:
.PHONY : CMakeFiles/optimizer.dir/parser.cpp.o.requires

CMakeFiles/optimizer.dir/parser.cpp.o.provides: CMakeFiles/optimizer.dir/parser.cpp.o.requires
	$(MAKE) -f CMakeFiles/optimizer.dir/build.make CMakeFiles/optimizer.dir/parser.cpp.o.provides.build
.PHONY : CMakeFiles/optimizer.dir/parser.cpp.o.provides

CMakeFiles/optimizer.dir/parser.cpp.o.provides.build: CMakeFiles/optimizer.dir/parser.cpp.o

CMakeFiles/optimizer.dir/simple_ast.cpp.o: CMakeFiles/optimizer.dir/flags.make
CMakeFiles/optimizer.dir/simple_ast.cpp.o: /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/simple_ast.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/optimizer.dir/simple_ast.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/optimizer.dir/simple_ast.cpp.o -c /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/simple_ast.cpp

CMakeFiles/optimizer.dir/simple_ast.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/optimizer.dir/simple_ast.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/simple_ast.cpp > CMakeFiles/optimizer.dir/simple_ast.cpp.i

CMakeFiles/optimizer.dir/simple_ast.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/optimizer.dir/simple_ast.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/simple_ast.cpp -o CMakeFiles/optimizer.dir/simple_ast.cpp.s

CMakeFiles/optimizer.dir/simple_ast.cpp.o.requires:
.PHONY : CMakeFiles/optimizer.dir/simple_ast.cpp.o.requires

CMakeFiles/optimizer.dir/simple_ast.cpp.o.provides: CMakeFiles/optimizer.dir/simple_ast.cpp.o.requires
	$(MAKE) -f CMakeFiles/optimizer.dir/build.make CMakeFiles/optimizer.dir/simple_ast.cpp.o.provides.build
.PHONY : CMakeFiles/optimizer.dir/simple_ast.cpp.o.provides

CMakeFiles/optimizer.dir/simple_ast.cpp.o.provides.build: CMakeFiles/optimizer.dir/simple_ast.cpp.o

CMakeFiles/optimizer.dir/optimizer.cpp.o: CMakeFiles/optimizer.dir/flags.make
CMakeFiles/optimizer.dir/optimizer.cpp.o: /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/optimizer.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/optimizer.dir/optimizer.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/optimizer.dir/optimizer.cpp.o -c /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/optimizer.cpp

CMakeFiles/optimizer.dir/optimizer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/optimizer.dir/optimizer.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/optimizer.cpp > CMakeFiles/optimizer.dir/optimizer.cpp.i

CMakeFiles/optimizer.dir/optimizer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/optimizer.dir/optimizer.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer/optimizer.cpp -o CMakeFiles/optimizer.dir/optimizer.cpp.s

CMakeFiles/optimizer.dir/optimizer.cpp.o.requires:
.PHONY : CMakeFiles/optimizer.dir/optimizer.cpp.o.requires

CMakeFiles/optimizer.dir/optimizer.cpp.o.provides: CMakeFiles/optimizer.dir/optimizer.cpp.o.requires
	$(MAKE) -f CMakeFiles/optimizer.dir/build.make CMakeFiles/optimizer.dir/optimizer.cpp.o.provides.build
.PHONY : CMakeFiles/optimizer.dir/optimizer.cpp.o.provides

CMakeFiles/optimizer.dir/optimizer.cpp.o.provides.build: CMakeFiles/optimizer.dir/optimizer.cpp.o

# Object files for target optimizer
optimizer_OBJECTS = \
"CMakeFiles/optimizer.dir/parser.cpp.o" \
"CMakeFiles/optimizer.dir/simple_ast.cpp.o" \
"CMakeFiles/optimizer.dir/optimizer.cpp.o"

# External object files for target optimizer
optimizer_EXTERNAL_OBJECTS =

optimizer: CMakeFiles/optimizer.dir/parser.cpp.o
optimizer: CMakeFiles/optimizer.dir/simple_ast.cpp.o
optimizer: CMakeFiles/optimizer.dir/optimizer.cpp.o
optimizer: CMakeFiles/optimizer.dir/build.make
optimizer: CMakeFiles/optimizer.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable optimizer"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/optimizer.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/optimizer.dir/build: optimizer
.PHONY : CMakeFiles/optimizer.dir/build

CMakeFiles/optimizer.dir/requires: CMakeFiles/optimizer.dir/parser.cpp.o.requires
CMakeFiles/optimizer.dir/requires: CMakeFiles/optimizer.dir/simple_ast.cpp.o.requires
CMakeFiles/optimizer.dir/requires: CMakeFiles/optimizer.dir/optimizer.cpp.o.requires
.PHONY : CMakeFiles/optimizer.dir/requires

CMakeFiles/optimizer.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/optimizer.dir/cmake_clean.cmake
.PHONY : CMakeFiles/optimizer.dir/clean

CMakeFiles/optimizer.dir/depend:
	cd /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4/tools/optimizer /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer /mnt/data/src/emsdk_portable/emscripten/tag-1.34.4_64bit_optimizer/CMakeFiles/optimizer.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/optimizer.dir/depend

