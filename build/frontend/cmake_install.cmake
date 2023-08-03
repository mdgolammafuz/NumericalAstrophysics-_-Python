# Install script for directory: /Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/latex/")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/latex" TYPE DIRECTORY DIR_PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES "")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/manual/")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/manual" TYPE DIRECTORY DIR_PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES "")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/manual/algorithms/")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/manual/algorithms" TYPE DIRECTORY DIR_PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES "")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/manual/properties/")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/manual/properties" TYPE DIRECTORY DIR_PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES "")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/latex/preamble.tex")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/latex" TYPE FILE FILES "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/common/preamble.tex")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/manual/algorithms/asym.cnb;/usr/local/share/cadabra2/manual/algorithms/canonicalise.cnb;/usr/local/share/cadabra2/manual/algorithms/collect_factors.cnb;/usr/local/share/cadabra2/manual/algorithms/collect_terms.cnb;/usr/local/share/cadabra2/manual/algorithms/combine.cnb;/usr/local/share/cadabra2/manual/algorithms/complete.cnb;/usr/local/share/cadabra2/manual/algorithms/decompose.cnb;/usr/local/share/cadabra2/manual/algorithms/decompose_product.cnb;/usr/local/share/cadabra2/manual/algorithms/distribute.cnb;/usr/local/share/cadabra2/manual/algorithms/drop_weight.cnb;/usr/local/share/cadabra2/manual/algorithms/einsteinify.cnb;/usr/local/share/cadabra2/manual/algorithms/eliminate_kronecker.cnb;/usr/local/share/cadabra2/manual/algorithms/eliminate_metric.cnb;/usr/local/share/cadabra2/manual/algorithms/eliminate_vielbein.cnb;/usr/local/share/cadabra2/manual/algorithms/epsilon_to_delta.cnb;/usr/local/share/cadabra2/manual/algorithms/evaluate.cnb;/usr/local/share/cadabra2/manual/algorithms/expand.cnb;/usr/local/share/cadabra2/manual/algorithms/expand_delta.cnb;/usr/local/share/cadabra2/manual/algorithms/expand_diracbar.cnb;/usr/local/share/cadabra2/manual/algorithms/expand_dummies.cnb;/usr/local/share/cadabra2/manual/algorithms/expand_power.cnb;/usr/local/share/cadabra2/manual/algorithms/explicit_indices.cnb;/usr/local/share/cadabra2/manual/algorithms/factor_in.cnb;/usr/local/share/cadabra2/manual/algorithms/factor_out.cnb;/usr/local/share/cadabra2/manual/algorithms/fierz.cnb;/usr/local/share/cadabra2/manual/algorithms/integrate_by_parts.cnb;/usr/local/share/cadabra2/manual/algorithms/join_gamma.cnb;/usr/local/share/cadabra2/manual/algorithms/keep_weight.cnb;/usr/local/share/cadabra2/manual/algorithms/lower_free_indices.cnb;/usr/local/share/cadabra2/manual/algorithms/lr_tensor.cnb;/usr/local/share/cadabra2/manual/algorithms/map_sympy.cnb;/usr/local/share/cadabra2/manual/algorithms/meld.cnb;/usr/local/share/cadabra2/manual/algorithms/product_rule.cnb;/usr/local/share/cadabra2/manual/algorithms/raise_free_indices.cnb;/usr/local/share/cadabra2/manual/algorithms/reduce_delta.cnb;/usr/local/share/cadabra2/manual/algorithms/rename_dummies.cnb;/usr/local/share/cadabra2/manual/algorithms/replace_match.cnb;/usr/local/share/cadabra2/manual/algorithms/rewrite_indices.cnb;/usr/local/share/cadabra2/manual/algorithms/simplify.cnb;/usr/local/share/cadabra2/manual/algorithms/slot_asym.cnb;/usr/local/share/cadabra2/manual/algorithms/sort_product.cnb;/usr/local/share/cadabra2/manual/algorithms/sort_spinors.cnb;/usr/local/share/cadabra2/manual/algorithms/sort_sum.cnb;/usr/local/share/cadabra2/manual/algorithms/split_gamma.cnb;/usr/local/share/cadabra2/manual/algorithms/split_index.cnb;/usr/local/share/cadabra2/manual/algorithms/substitute.cnb;/usr/local/share/cadabra2/manual/algorithms/take_match.cnb;/usr/local/share/cadabra2/manual/algorithms/untrace.cnb;/usr/local/share/cadabra2/manual/algorithms/unwrap.cnb;/usr/local/share/cadabra2/manual/algorithms/vary.cnb;/usr/local/share/cadabra2/manual/algorithms/young_project_product.cnb;/usr/local/share/cadabra2/manual/algorithms/young_project_tensor.cnb;/usr/local/share/cadabra2/manual/algorithms/zoom.cnb")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/manual/algorithms" TYPE FILE FILES
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/asym.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/canonicalise.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/collect_factors.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/collect_terms.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/combine.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/complete.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/decompose.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/decompose_product.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/distribute.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/drop_weight.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/einsteinify.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/eliminate_kronecker.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/eliminate_metric.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/eliminate_vielbein.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/epsilon_to_delta.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/evaluate.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/expand.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/expand_delta.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/expand_diracbar.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/expand_dummies.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/expand_power.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/explicit_indices.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/factor_in.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/factor_out.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/fierz.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/integrate_by_parts.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/join_gamma.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/keep_weight.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/lower_free_indices.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/lr_tensor.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/map_sympy.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/meld.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/product_rule.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/raise_free_indices.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/reduce_delta.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/rename_dummies.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/replace_match.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/rewrite_indices.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/simplify.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/slot_asym.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/sort_product.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/sort_spinors.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/sort_sum.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/split_gamma.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/split_index.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/substitute.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/take_match.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/untrace.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/unwrap.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/vary.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/young_project_product.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/young_project_tensor.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/algorithms/zoom.cnb"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/cadabra2/manual/properties/Accent.cnb;/usr/local/share/cadabra2/manual/properties/AntiCommuting.cnb;/usr/local/share/cadabra2/manual/properties/AntiSymmetric.cnb;/usr/local/share/cadabra2/manual/properties/Commuting.cnb;/usr/local/share/cadabra2/manual/properties/CommutingAsProduct.cnb;/usr/local/share/cadabra2/manual/properties/CommutingAsSum.cnb;/usr/local/share/cadabra2/manual/properties/Coordinate.cnb;/usr/local/share/cadabra2/manual/properties/DAntiSymmetric.cnb;/usr/local/share/cadabra2/manual/properties/Depends.cnb;/usr/local/share/cadabra2/manual/properties/Derivative.cnb;/usr/local/share/cadabra2/manual/properties/Determinant.cnb;/usr/local/share/cadabra2/manual/properties/Diagonal.cnb;/usr/local/share/cadabra2/manual/properties/DiracBar.cnb;/usr/local/share/cadabra2/manual/properties/Distributable.cnb;/usr/local/share/cadabra2/manual/properties/EpsilonTensor.cnb;/usr/local/share/cadabra2/manual/properties/FilledTableau.cnb;/usr/local/share/cadabra2/manual/properties/GammaMatrix.cnb;/usr/local/share/cadabra2/manual/properties/ImplicitIndex.cnb;/usr/local/share/cadabra2/manual/properties/IndexInherit.cnb;/usr/local/share/cadabra2/manual/properties/Indices.cnb;/usr/local/share/cadabra2/manual/properties/Integer.cnb;/usr/local/share/cadabra2/manual/properties/InverseMetric.cnb;/usr/local/share/cadabra2/manual/properties/InverseVielbein.cnb;/usr/local/share/cadabra2/manual/properties/KroneckerDelta.cnb;/usr/local/share/cadabra2/manual/properties/LaTeXForm.cnb;/usr/local/share/cadabra2/manual/properties/Metric.cnb;/usr/local/share/cadabra2/manual/properties/NonCommuting.cnb;/usr/local/share/cadabra2/manual/properties/PartialDerivative.cnb;/usr/local/share/cadabra2/manual/properties/RiemannTensor.cnb;/usr/local/share/cadabra2/manual/properties/SatisfiesBianchi.cnb;/usr/local/share/cadabra2/manual/properties/SelfAntiCommuting.cnb;/usr/local/share/cadabra2/manual/properties/SelfCommuting.cnb;/usr/local/share/cadabra2/manual/properties/SelfNonCommuting.cnb;/usr/local/share/cadabra2/manual/properties/SortOrder.cnb;/usr/local/share/cadabra2/manual/properties/Spinor.cnb;/usr/local/share/cadabra2/manual/properties/Symbol.cnb;/usr/local/share/cadabra2/manual/properties/Symmetric.cnb;/usr/local/share/cadabra2/manual/properties/Tableau.cnb;/usr/local/share/cadabra2/manual/properties/TableauSymmetry.cnb;/usr/local/share/cadabra2/manual/properties/Trace.cnb;/usr/local/share/cadabra2/manual/properties/Vielbein.cnb;/usr/local/share/cadabra2/manual/properties/Weight.cnb;/usr/local/share/cadabra2/manual/properties/WeightInherit.cnb")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/cadabra2/manual/properties" TYPE FILE FILES
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Accent.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/AntiCommuting.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/AntiSymmetric.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Commuting.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/CommutingAsProduct.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/CommutingAsSum.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Coordinate.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/DAntiSymmetric.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Depends.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Derivative.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Determinant.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Diagonal.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/DiracBar.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Distributable.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/EpsilonTensor.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/FilledTableau.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/GammaMatrix.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/ImplicitIndex.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/IndexInherit.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Indices.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Integer.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/InverseMetric.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/InverseVielbein.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/KroneckerDelta.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/LaTeXForm.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Metric.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/NonCommuting.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/PartialDerivative.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/RiemannTensor.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/SatisfiesBianchi.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/SelfAntiCommuting.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/SelfCommuting.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/SelfNonCommuting.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/SortOrder.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Spinor.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Symbol.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Symmetric.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Tableau.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/TableauSymmetry.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Trace.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Vielbein.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/Weight.cnb"
    "/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/cadabra2/frontend/../core/properties/WeightInherit.cnb"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/mdgolammafuz/Desktop/Numerical_Astrophysics/build/frontend/gtkmm/cmake_install.cmake")

endif()

