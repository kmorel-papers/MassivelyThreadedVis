cmake_minimum_required(VERSION 2.8)

project(MassivelyThreadedVis NONE)

include(UseLATEX.cmake)

add_latex_document(MassivelyThreadedVis.tex
  BIBFILES MassivelyThreadedVis.bib
  )
