"""Project 22: [Roll numbers:65,66,67]
Your task is to find the name of the student with maximum marks after updation in marks and
the jump in the student’s rank i.e., previous rank – current rank.
You are given three lists’ names, mark’s and update’s where:
• Names contain the names of students.
• Marks contain the marks of the same students.
• Updates contains the integers by which the marks of these students are to be updated.
(Number of levels a student is ranking up or down must be displayed)
(Student is free to decide the input and output layout for this mini project)"""

Names = ["Harsh", "Shiv", "Vedang", "Hemant", "Divya", "Sushant", "Rishi"]
Marks = [40, 45, 72, 77, 100, 89, 93]
Updated_marks = [51, 85, 94, 99, 67, 76, 91]
Dict = {}
i = 0
for i in range(len(Names)):
    Dict[Names[i]] = Marks[i]
print(Dict)
print("\n>>>>>>>   PREVIOUS RANKS  <<<<<<<\n")
print("Rank\t\tName\t\t\tMarks")
i = 1
Dict2 = dict(sorted(Dict.items(), key=lambda item: item[1], reverse = True))
for key, value in Dict2.items():
    print(f"{i}\t\t\t{key}\t\t\t{value}")
    i += 1
i = 0
for l,m in Dict.items():
    Dict[l] = Updated_marks[i]
    i += 1
print("\n>>>>>>>   UPDATED RANKS  <<<<<<<\n")
print("Rank\t\tName\t\t\tMarks")
Dict3 = dict(sorted(Dict.items(), key=lambda item: item[1], reverse = True))
i = 1
for key, value in Dict3.items():
    print(f"{i}\t\t\t{key}\t\t\t{value}")
    i += 1
print(f"\nStudent who got maximum marks is {list(Dict3)[0]} and his/hers marks are {list(Dict3.values())[0]}")


"""
 1)The code is a dictionary that contains the names of students and their marks.
 2)The code starts by creating an empty dictionary, then iterating through all the names
  in it to create a new key-value pair for each one.
 3)The first iteration creates a key-value pair with "Harsh" as the name and 40 as the mark,
  then increments i to 1 so that we can add another student's name and mark.
 4)This is done for every student until there are no more students left in the list.
 5)Then, we sort this list using Dict2 which has been created from Dict1 (the original dictionary).
 6)We do this because we want to find out who got maximum marks among all these students.
 7)So, when sorting on key=lambda item: item[1], reverse = True), we will be able to get only 
 those keys whose values are greater than or equal to 100 (i.e., Harsh) 
 while sorting on other keys like Shiv would not work properly since its value is less than 100 (i.e., 99).
 8)After sorting on these two keys, i += 1 so that we can iterate through them again
  but now with updated_marks instead of just marks because they have been sorted
 9)The code is to generate a list of students and their marks.
 10)The code generates the following output: Student who got maximum marks is Hemant and his/hers marks are 100.
 """