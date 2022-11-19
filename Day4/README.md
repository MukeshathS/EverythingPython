Day 4 - 
-----
Challenge 4.1 - 
-------------
Given the names and grades for each student in a class of N students,  
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,  
order their names alphabetically and print each name on a new line.

Example -  
records = [["chi",20.0],["beta",50.0],["alpha",50.0]]  

The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0.  
There are two students with that score: ["beta","alpha"].  
Ordered alphabetically, the names are printed as:  

alpha  
beta

Challenge 4.2 - 
-------------

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.  
Print the average of the marks array for the student name provided, showing 2 places after the decimal.  

Input Format -  

The first line contains the integer , the number of students' records.  
The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.  

Challenge 4.3 - 
-------------

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.    
It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.   
A leap year contains a leap day.  

In the Gregorian calendar, three conditions are used to identify leap years:   

The year can be evenly divided by 4, is a leap year, unless:  
- The year can be evenly divided by 100, it is NOT a leap year, unless:
- The year is also evenly divisible by 400. Then it is a leap year.
- This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task -  

Given a year, determine whether it is a leap year.  
If it is a leap year, return the Boolean True, otherwise return False.  

Challenge 4.4 - 
-------------

Consider a list (list = []). You can perform the following commands:

- insert i e: Insert integer e at position i.
- print: Print the list.
- remove e: Delete the first occurrence of integer e.
- append e: Insert integer e at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.
- Initialize your list and read in the value of n followed by n lines of commands where  
each command will be of the 7 types listed above. Iterate through each command in order  
and perform the corresponding operation on your list.


Challenge 4.5 - 
-------------

You are given a string and your task is to swap cases.  
In other words, convert all lowercase letters to uppercase letters and vice versa.

Example -   
Input -  HackerRank.com presents "Pythonist 2".   
Output -  hACKERrANK.COM PRESENTS "pYTHONIST 2".  

