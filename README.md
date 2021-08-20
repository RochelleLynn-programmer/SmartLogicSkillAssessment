# SmartLogicSkillAssessment
Skill Assessment completed for SmartLogic Internship Program

The purpose of this assessment is to take data from files that are formatted in 3 different styles, reformat them, and then sort them in 3 possible ways.

Chosen language was Python3.

This script can be ran from the command line.

In order to do so, when inside of the directory in your CLI, input the following arguments:

python assessment.py [list of file names]

The above command will by default sort files by gender, then last name, and print sorted and formatted information into the terminal

***
Flags for different behavior:

-o or --output followed by 1, 2, or 3

    1: Sorts first on gender, then on last name

    2: Sorts on date of birth, then last name

    3: Sorts last name in descending order


-s or --summary

    This command will instruct the script to store the output into OutputSummary.txt

---

Expected formatting for input files:


Pipe Delimited Files

    LastName | FirstName | MiddleInitial | Gender | FavoriteColor | DateOfBirth


Comma Delimited Files

    LastName, FirstName, Gender, FavoriteColor, DateOfBirth


Space Delimited Files

    LastName FirstName MiddleInitial Gender DateOfBirth FavoriteColor

***


Expected Format after processing:

    LastName FirstName Gender DateOfBirth(M/D/YYYY) FavoriteColor