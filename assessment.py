#!/usr/bin/env python3

"""
Skill Assessment for Smart Logic, chosen language is Python 3
"""

__author__ = "Rochelle Edwards rochellelynn.programmer@gmail.com"

import sys
import argparse
import re

def PipeFormat(contents):
  """Doc sting to get filled out"""
  temp_list = []
  regexp_pipe = r"(\w+)\W+(\w+)\W+\w\W+(\w)\W+(\w+)\W+(\d+/\d+/\d+)"
  reg_return = re.findall(regexp_pipe, contents)

  for item in reg_return:
    (last, first, gender, color, dob) = item
    if gender == "M":
      gender = "Male"
    else:
      gender = "Female"
    temp_list.append([last, first, gender, dob, color])
  return temp_list

def CommaFormat(contents):
  """Doc string to be filled out"""
  temp_list = []
  regexp_comma = r"(\w+)\W\s(\w+)\W\s(\w+)\W\s(\w+)\W\s(\d+/\d+/\d+)"
  reg_return = re.findall(regexp_comma, contents)

  for item in reg_return:
    (last, first, gender, color, dob) = item
    temp_list.append([last, first, gender, dob, color])
  return temp_list

def SpaceFormat(contents):
  """Doc string to be filled out"""
  temp_list = []
  regexp_comma = r"(\w+)\s(\w+)\s\w\s(\w)\s(\d+/\d+/\d+)\s(\w+)"
  reg_return = re.findall(regexp_comma, contents)

  for item in reg_return:
    (last, first, gender, dob, color) = item
    if gender == "M":
      gender = "Male"
    else:
      gender = "Female"
    temp_list.append([last, first, gender, dob, color])
  return temp_list


def CheckDelimiterAndFormat(filename):
  """doc string to be filled out"""
  with open(filename, 'r') as f:
    contents = f.read()

  contents = re.sub("-", "/", contents)
  pipe_sort = re.search(r"\|", contents)
  comma_sort = re.search(r",", contents)

  if pipe_sort:
    pipe_formated_list = PipeFormat(contents)
    return pipe_formated_list
  elif comma_sort:
    comma_formated_list = CommaFormat(contents)
    return comma_formated_list
  else:
    space_formatted_list = SpaceFormat(contents)
    return space_formatted_list


def ProcessFiles(file_list, desired_output):
  """Doc String to be filled out"""
  list_to_sort = []
  for file in file_list:
    formated_list = CheckDelimiterAndFormat(file)
    list_to_sort.extend(formated_list)
  print(list_to_sort)

  print(desired_output)


def create_parser():
  """Creates a command line argument parser with one positional argument and 
  two optional flags with default values.
  """

  parser = argparse.ArgumentParser(
    description=
    """Extracts data from files and sorts it based of chosen output flag. 
    Once files are sorted and combined into a single list, data is either
    printed into the terminal or stored into a summary file.
    """
    )

  parser.add_argument("files", nargs="+", 
    help="Takes in a list of files from the command line intended to be sorted"
    )

  parser.add_argument("-o", "--output", default=1, 
    help="""Determines which sort style the output will be.
    Defaults to Output 1 if flag is not raised"""
    )

  parser.add_argument("-s", "--summary", action="store_true", 
  help="""If summary flag is raised, sorted file data will be stored into a new 
  file with in this directory. If it is not, data will print to the terminal.
  """
  )
  return parser


def main(args):
  """This Doc string needs to be filled out before turing in"""
  parser = create_parser()
  ns = parser.parse_args(args)

  if not ns:
        parser.print_usage()
        sys.exit(1)

  file_list = ns.files
  desired_output = int(ns.output)
  summary = ns.summary

  ProcessFiles(file_list = file_list, desired_output = desired_output)



if __name__ == '__main__':
    main(sys.argv[1:])
