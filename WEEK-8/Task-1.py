d=int(input("Enter the number of students: "))

for i in range(d):  
   st_name=input("Enter the name of student: ")  
   st_roll_no=int(input("Enter the roll number of student: "))
   t_marks = int(input("Enter total Marks:"))
   obt_marks =int(input("Enter Obtained Marks: "))

   percentage=(obt_marks/t_marks)*100
   print("RESULT")
   print("Name:",st_name)
   print("Roll No:",st_roll_no)
   print("Your Percentage: ",percentage)

   if t_marks == 0 or obt_marks >= t_marks:
    print("Invalid")
   if percentage >= 90:
    print("Grade:A")
   elif percentage >= 85:
    print("Grade:A-") 
   elif percentage >= 80:
    print("Grade:B+") 
   elif percentage >= 75:
    print("Grade:B") 
   elif percentage >= 70:
    print("Grade:B-")
   elif percentage >= 65:
    print("Grade:C+")
   elif percentage >= 60:
    print("Grade:C")
   elif percentage >= 55:
    print("Grade:C-")
   elif percentage >= 50:
    print("Grade:D")
   else:
    print("Grade:F")      

