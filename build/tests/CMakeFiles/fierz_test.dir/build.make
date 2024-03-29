# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.27.1/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.27.1/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build

# Utility rule file for fierz_test.

# Include any custom commands dependencies for this target.
include tests/CMakeFiles/fierz_test.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/CMakeFiles/fierz_test.dir/progress.make

tests/CMakeFiles/fierz_test: tests/fierz.cdb

tests/fierz.cdb: /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/examples/fierz.cnb
tests/fierz.cdb: /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/client_server/cadabra2html.cc
tests/fierz.cdb: /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/core/DataCell.hh
tests/fierz.cdb: /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/core/DataCell.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Creating fierz notebook..."
	cd /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/tests && ../core/cadabra2cadabra /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/examples/fierz.cnb /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/tests/fierz.cdb

fierz_test: tests/CMakeFiles/fierz_test
fierz_test: tests/fierz.cdb
fierz_test: tests/CMakeFiles/fierz_test.dir/build.make
.PHONY : fierz_test

# Rule to build all files generated by this target.
tests/CMakeFiles/fierz_test.dir/build: fierz_test
.PHONY : tests/CMakeFiles/fierz_test.dir/build

tests/CMakeFiles/fierz_test.dir/clean:
	cd /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/tests && $(CMAKE_COMMAND) -P CMakeFiles/fierz_test.dir/cmake_clean.cmake
.PHONY : tests/CMakeFiles/fierz_test.dir/clean

tests/CMakeFiles/fierz_test.dir/depend:
	cd /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2 /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/tests /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/tests /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/tests/CMakeFiles/fierz_test.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : tests/CMakeFiles/fierz_test.dir/depend

