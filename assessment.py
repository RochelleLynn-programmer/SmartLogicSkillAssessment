#!/usr/bin/env python3

"""
Skill Assessment for Smart Logic, chosen language is Python 3
"""

__author__ = "Rochelle Edwards rochellelynn.programmer@gmail.com"

import sys
import argparse
import re
from datetime import datetime


def ListJoiner(list):
  """ Takes in a nested list, returns a list of strings """
  temp_list = []

  for item in list:
    i = " ".join(item)
    temp_list.append(i)

  return temp_list


def SortGenderThenLast(list):
  """ Returns a list sorted by gender (females before males),
  then by last name ascending """
  sorted_list = sorted(list, key=lambda i: (i[2], i[0]))
  joined = ListJoiner(sorted_list)

  return joined


def SortDobThenLast(list):
  """ Returns a list sorted by ascending DOB, then by last name ascending"""
  sorted_list = sorted(list,
                      key=lambda i: (datetime.strptime(i[3], '%m/%d/%Y'), i[0]))
  joined = ListJoiner(sorted_list)

  return joined


def SortLast(list):
  """ Returns a list sorted by last name, descending"""
  sorted_list = sorted(list, key=lambda i: i[0], reverse=True)
  joined = ListJoiner(sorted_list)

  return joined


def PipeFormat(contents):
  """Takes in contents of txt file that is delimited with pipes, orders data
  appropriately, converts gender letters into strings, and returns a list"""
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
  """Takes in contents of txt file that is delimited with commas, orders data
  appropriately, and returns a list"""
  temp_list = []
  regexp_comma = r"(\w+)\W\s(\w+)\W\s(\w+)\W\s(\w+)\W\s(\d+/\d+/\d+)"
  reg_return = re.findall(regexp_comma, contents)

  for item in reg_return:
    (last, first, gender, color, dob) = item
    temp_list.append([last, first, gender, dob, color])

  return temp_list


def SpaceFormat(contents):
  """Takes in contents of txt file that is delimited with spaces, orders data
  appropriately, converts gender letters into strings, and returns a list"""
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
  """Takes in a file, runs various reg exps on it to see how it is delimited,
  calls appropraite format function, returns properly formated list"""

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
  """Takes in a file list, calls function to check delimiter and format, extends
  returned list into a list that needs to be sorted. Once all files are 
  formatted, lists are sorted based off what the desired output number is. Once
  list is formatted and sorted, list is returned"""
  list_to_sort = []
  list_to_return = [f"Output {desired_output}:"]

  for file in file_list:
    formated_list = CheckDelimiterAndFormat(file)
    list_to_sort.extend(formated_list)

  if desired_output == 1:
    sorted_list = SortGenderThenLast(list_to_sort)
    list_to_return.extend(sorted_list)
  elif desired_output == 2:
    sorted_list = SortDobThenLast(list_to_sort)
    list_to_return.extend(sorted_list)
  else:
    sorted_list = SortLast(list_to_sort)
    list_to_return.extend(sorted_list)

  return list_to_return


def DisplayData(list, summary):
  """Takes in a formatted and sorted list, and depending on whether or not the
  summary flag is raise, data is printed to the terminal or saved into 
  OutputSummary.txt"""
  if summary == False:
    for item in list:
      print(item)
  else:
    for item in list:
      with open('OutputSummary.txt', "a") as f:
        f.write(f"{item} \n")
    with open('OutputSummary.txt', "a") as f:
        f.write("\n")


def create_parser():
  """Creates a command line argument parser with one positional argument and 
  two optional flags with default values."""

  parser = argparse.ArgumentParser(
    description=
    """Extracts data from files and sorts it based of chosen output flag. 
    Once files are sorted and combined into a single list, data is either
    printed into the terminal or stored into a summary file."""
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
  file with in this directory. If it is not, data will print to the terminal."""
  )

  return parser


def main(args):
  """Main function of assessment.py. It calls function to create parser, creates
  the namespace, extracts variables from namespace, notifies user if arguments
  are not provided in the command line. If CLI arguments meet mandatory 
  minimum requirements, files get processed and outputted accordingly and
  presented based of user's choice of summary"""
  parser = create_parser()
  ns = parser.parse_args(args)

  if not ns:
        parser.print_usage()
        sys.exit(1)

  file_list = ns.files
  desired_output = int(ns.output)
  summary = ns.summary

  processed_files = ProcessFiles(file_list, desired_output)
  DisplayData(processed_files, summary)


if __name__ == '__main__':
    main(sys.argv[1:])
