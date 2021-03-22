# Ameer Al-Shamaa
# 18/03/2021
# swapDuty.py
# Master program in which swap's yard duties with other staff members.

# a function to detect any numbers found within any given string
def hasNumbers(inputString):
   return any(char.isdigit() for char in inputString)

# Information regarding the teacher who is requesting this swap.
teacherRequestingName = input("What is the name of the teacher requesting the change?\n") # Name of the teacher requesting the swap
teacherRequestingDay = input(f"What day is the yard duty of {teacherRequestingName} scheduled on?\n") # current day of the teacher requesing the swap
teacherRequestingTime = input(f"Which section of the day is this shift during?\n") # Current shift time of the the teacher requesting the swap
teacherRequestingDuty = input(f"What is the current shift duty of {teacherRequestingName}?\n") # Role of the teacher requesting the swap

# Information regarding the teacher who is going to swap with the teacher requesting this change.
secondTeacherName = input("What is the name of the second teacher?\n") # Name of the swapping teacher
secondTeacherDay = input(f"What day is the yard duty of {secondTeacherName} scheduled on?\n") # Current shift the second teacher is one right now
secondTeacherTime = input(f"Which section of the day is this shift during?\n") # Time of the second's teacher shift
secondTeacherDuty = input(f"What is the current shift duty of {secondTeacherName}?\n") # Role of the second teacher shift

# A conditional checker to see if the name of who is going to swap with who is the same name, avoiding unnessecary overlapping
if(teacherRequestingName == teacherRequestingName and secondTeacherName == teacherRequestingName):
    raise Exception("Error! You are currently trying to swap shifts with the same person!\nPlease specifiy two different teachers.")

# A conditional type checker (validation techniques) to see if the name provided is contains any numbers (calling the function hasNumbers())
if(hasNumbers(teacherRequestingName) == True or hasNumbers(secondTeacherName) == True):
    raise Exception("Error! Number's detected in the names of one of the teachers. Only characters are acceptable.")

# Outputing the final results after the checkers have ran through everything.
print("✅ Success")
print(\
    f"Yard time duties have been swapped, {teacherRequestingName} has swapped shifts with {secondTeacherName}:\n"
    f"{secondTeacherName} is now incharge of {teacherRequestingDuty} on {teacherRequestingDay} during {teacherRequestingTime}\n"
    f"{teacherRequestingName} is now incharge of {secondTeacherDuty} on {secondTeacherDay} during {secondTeacherTime}"
)
