import time



#=========QUESTION BANK=========

questions = [
   {
        "id": 1,
        "subject": "Biology",
        "question": "During The Light Reaction Of Photosynthesis,ATP Is Produced Through :",

        "choices": {
            "A": "Glycolysis",
            "B": "Photophosphorylation",
            "C": "Oxidative Phosphorylation",
            "D": "Fermentation"
        },

        "answer": "B"
    },

    {
        "id": 2,
        "subject": "Chemistry",
        "question": "The Oxidation Number Of Sulfur In H2SO4 Is :",

        "choices": {
            "A": "+4",
            "B": "+6",
            "C": "+2",
            "D": "-2"
        },

        "answer": "B"
    },

    {
        "id": 3,
        "subject": "Physics",
        "question": "The Escape Velocity From Earth Depends Upon :",

        "choices": {
            "A": "Mass Of The Object",
            "B": "Radius Of Earth",
            "C": "Mass And Radius Of Earth",
            "D": "Gravitational Constant"
        },

        "answer": "C"
    },

    {
        "id": 4,
        "subject": "English",
        "question": "Which Word Is Closest In Meaning To 'Meticulous'?",

        "choices": {
            "A": "Careless",
            "B": "Detailed",
            "C": "Confused",
            "D": "Brave"
        },

        "answer": "B"
    },

    {
        "id": 5,
        "subject": "History",
        "question": "Who dissolved the national assembly in 1977?",

        "choices": {
            "A": "Zulfikar Ali Bhutto",
            "B": "Muhammad Zia-ul-Haq",
            "C": "General Ayub Khan",
            "D": "Ferdousi Iqbal"
        },

        "answer": "B"
    },

    {
        "id": 6,
        "subject": "General Knowledge",
        "question": "Which event officially marked the beginning of World War I?",

        "choices": {
            "A": "Assassination of Archduke Franz Ferdinand",
            "B": "Britain declaring war on Germany",
            "C": "Austria-Hungary declaring war on Serbia",
            "D": "Germany invading Belgium"
        },

        "answer": "C"
    },

    {
        "id": 7,
        "subject": "Biology",
        "question": "The name 'BELLIS PERENNIS' refers to :",    

        "choices": {
            "A": "Rose",
            "B": "Sunflower",
            "C": "Jasmine",
            "D": "Daisy"
        },

        "answer": "D"
    },

    {
        "id": 8,
        "subject": "Programming",
        "question": "Which loop repeats until condition becomes false?",

        "choices": {
            "A": "for",
            "B": "while",
            "C": "repeat",
            "D": "loop"
        },

        "answer": "B"
    },

    {
        "id": 9,
        "subject": "Chemistry",
        "question": "Which Of the following compounds can show geometrical isomerism?",

        "choices": {
            "A": "CH4",
            "B": "C2H6",
            "C": "C2H4CL2",
            "D": "C2H2"
        },

        "answer": "C"
    },

    {
        "id": 10,
        "subject": "Physics",
        "question": "Accordin to Guass's Law,electric field inside a uniforomly charged sphere varies as:",

        "choices": {
            "A": "1/r^2 ",
            "B": "r",
            "C": "Constant",
            "D": "Zero Everywhere"
        },

        "answer": "B"
    }

]            

#=========CONSTANTS=========

CORRECT_MARKS = 4
WRONG_MARKS = -1
SKIP_MARKS = 0

#=========RESULT STORAGE=========


all_results = []




#=========VIEW RULES=========

def view_rules():



    print("\n========== EXAM RULES ==========")
    print("1. The exam consists of 10 multiple-choice questions.")
    print("2. Enter the option (A, B, C, D) for your answer or 'S' to skip the question.")
    print("3. Each correct answer awards 4 marks.")
    print("4. Each wrong answer deducts 1 mark.")
    print("5. Skipped questions do not affect the score.")
    print("6. You can type 'SUBMIT' to end the exam early.")
    print("7. No negative marking for skipped questions.")





#========VIEW QUESTIONS=========

def view_questions():
    
    if len(questions) == 0:
        print("No Questions Available")
        return

    for q in questions:

        print("\n--------------------------------")
        print("Question ID:", q["id"])
        print("Subject:", q["subject"])
        print("Question:", q["question"])

        for key, value in q["choices"].items():
            print(key, ":", value)

        print("Correct Answer:", q["answer"])


#========ADD QUESTION=========

def add_question():
    
    subject = input("Enter Subject: ")

    question_text = input("Enter Question: ")

    choices = {}

    choices["A"] = input("Enter Option A: ")
    choices["B"] = input("Enter Option B: ")
    choices["C"] = input("Enter Option C: ")
    choices["D"] = input("Enter Option D: ")

    answer = input("Enter Correct Answer (A/B/C/D): ").upper()

    new_question = {

        "id": len(questions) + 1,
        "subject": subject,
        "question": question_text,
        "choices": choices,
        "answer": answer

    }

    questions.append(new_question)

    print("Question Added Successfully")


#========DELETE QUESTIONS=========

def delete_questions():

    view_questions()

    try:
         
        qid = int(input("\nEnter Question ID to Delete: "))

        for i in range(len(questions)):

            if questions[i]["id"] == qid:

                questions.pop(i)

                print("Question Deleted Successfully")
                return

        print("Question Not Found")

    except:
        print("Invalid Input")    


#========QUESTION STATISTICS=========

def question_statistics():

    print("\n========== QUESTION STATISTICS ==========")

    print("Total Questions:", len(questions))

    subjects = {}

    for q in questions:

        sub = q["subject"]

        if sub in subjects:
            subjects[sub] += 1
        else:
            subjects[sub] = 1

    for key, value in subjects.items():
        print(key, ":", value)


#========VIEW ALL STUDENT RESULTS=========
 
def view_all_results(): 
    
    if len(all_results) == 0:

        print("No Results Available")
        return

    print("\n========== ALL STUDENT RESULTS ==========")

    for result in all_results:

        print("\n--------------------------------")
        print("Name:", result["name"])
        print("Roll Number:", result["roll_no"])
        print("Score:", result["score"])
        print("Percentage:", result["percentage"])
        print("Grade:", result["grade"])
        print("Time:", result["time"])


#========VIEW DETAILED RESULT=========

def view_detailed_result():

    if len(all_results) == 0:
        print("No Results Available")
        return

    roll = input("Enter Roll Number: ")

    found = False

    for result in all_results:

        if result["roll_no"] == roll:

            found = True

            print("\n========== DETAILED RESULT ==========")

            print("Name:", result["name"])
            print("Roll:", result["roll_no"])
            print("Score:", result["score"])
            print("Percentage:", result["percentage"])
            print("Grade:", result["grade"])

            print("\nQuestion Review:")

            for review in result["review"]:
                print("\nQuestion:", review["question"])
                print("Student Answer:", review["student_answer"])
                print("Correct Answer:", review["correct_answer"])
                print("Result:", review["status"])

    if found == False:
        print("Result Not Found")    


#========CLASS STATISTICS=========

def class_statistics():
    
    if len(all_results) == 0:

        print("No Results Available")
        return

    scores = []

    pass_count = 0
    fail_count = 0

    grades = {
        "EXCELLENT": 0,
        "GOOD": 0,
        "AVERAGE": 0,
        "BELOW AVERAGE": 0
    }

    for result in all_results:

        scores.append(result["score"])

        if result["percentage"] >= 50:
            pass_count += 1
        else:
            fail_count += 1

        grades[result["grade"]] += 1

    print("\n========== CLASS STATISTICS ==========")

    print("Highest Score:", max(scores))
    print("Lowest Score:", min(scores))
    print("Average Score:", sum(scores) / len(scores))

    print("Pass Students:", pass_count)
    print("Fail Students:", fail_count)

    print("\nGrade Distribution:")

    for key, value in grades.items():
        print(key, ":", value)          


#=========CALCULATE RESULT=========

def calculate_result(name,roll_no,answers):

    correct = 0
    wrong   = 0
    skipped = 0

    review = []

    for idx in range(len(questions)):

        student_answer = answers.get(idx, "S")

        correct_answer = questions[idx]["answer"]

        if student_answer == "S":
            skipped += 1
            status = "Skipped"
        elif student_answer == correct_answer:  
            correct += 1
            status = "Correct"  
        else:        
            wrong += 1
            status = "Wrong"

        review.append({

            "question": questions[idx]["question"],
            "student_answer": student_answer,
            "correct_answer": correct_answer,
            "status": status

        })    

    score = (correct * CORRECT_MARKS) + (wrong * WRONG_MARKS)

    total_marks = len(questions) * CORRECT_MARKS

    percentage = (score / total_marks) * 100


    if percentage >= 80:
        grade = "EXCELLENT"

    elif percentage >= 65:
        grade = "GOOD"

    elif percentage >= 50:
        grade = "AVERAGE"

    else:
        grade = "BELOW AVERAGE"

    print("\n========== FINAL RESULT ==========")

    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skipped)

    print("Score:", score)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    result = {
        "name": name,
        "roll_no": roll_no,
        "score": score,
        "percentage": round(percentage, 2),
        "grade": grade,
        "time": time.strftime("%d-%m-%Y %H:%M:%S"),
        "review": review

    }

    all_results.append(result)    

#===================================
#     START EXAM
#===================================    
def start_exam(name,roll_no):

    answers = {}

    print("==========EXAM STARTED==========")   
    print("Best of Luck", name + "!")

    for idx in range(len(questions)):

        q = questions[idx]

        print("\n------------------------------------")
        print("Question", idx + 1)
        print(q["question"])
        
        for key, value in q["choices"].items():
            print(key,":",value)

        ans = input("Enter Answer: ").upper().strip()

        if ans == "SUBMIT" :
            break
        elif ans in ["A", "B", "C", "D","S"]:
            answers[idx] = ans

        else:
            print("INVALID INPUT")
            answers[idx] = "S"        

    calculate_result(name , roll_no, answers ) 

#========ADMIN MENU=========

def admin_menu():
    while True:
        
        print("\n------------------------------------")
        print("         ADMIN MENU           ")
        print("------------------------------------")


        print("1. View Questions")
        print("2. Add Question")
        print("3. Delete Questions")
        print("4. Question Statistics")
        print("5. View All Results")
        print("6. View Detailed Result")
        print("7. Class Statistics")
        print("8. Logout")  


        choice = input("Enter Choice: ")


        if choice == "1":

            view_questions()

        elif choice == "2":

            add_question()

        elif choice == "3":

            delete_questions()

        elif choice == "4":

            question_statistics()

        elif choice == "5":

            view_all_results()

        elif choice == "6":

            view_detailed_result()

        elif choice == "7":

            class_statistics()

        elif choice == "8":

            print("Logged Out")

            break   


        else:
            print("Invalid Choice")

#========ADMIN LOGIN=========

def admin_login():
    attempt = 3

    while attempt > 0:

        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if username == "ecat_admin" and password == "ecat@2026":
            print(" Login Successful \t Welcome Admin!")
            
            admin_menu()
                        
            return

        else:
            attempt -= 1
            print("Invalid Credentials")
            
            print("Attempts Left:", attempt)


    print("Account Locked")

#========STUDENT MENU=========

def student_menu(name,roll_no):

    while True:

        print("\n------------------------------------")
        print("         STUDENT MENU           ")
        print("------------------------------------")


        print("1. Start Exam")
        print("2. View Rules")
        print("3. Logout")  


        choice = input("Enter Choice: ")


        if choice == "1":

            start_exam(name, roll_no)

        elif choice == "2":

            view_rules()

        elif choice == "3":

            print("Logged Out")

            break   

        else:

            print("Invalid Choice")    

#========STUDENT LOGIN=========

def student_login():
    attempt = 3
    while attempt > 0:

        username = input("Enter Student Username: ")
        password = input("Enter Student Password: ")

        if username == "student" and password == "student123":

            print(" Login Successful \t Welcome !")

            name=input("Enter Full Name: ")

            roll_no=input("Enter Roll Number: ")

            student_menu(name,roll_no)
                        
            return

        else:
            attempt -= 1
            print("Invalid Credentials")
            
            print("Attempts Left:", attempt)


    print("Account Locked") 


#=========MAIN MENU=========

def main_menu():

    while True:

        print("\n------------------------------------")
        print("       ECAT EXAM PORTAL")
        print("------------------------------------")

        print("1. Admin Portal")
        print("2. Student Portal")
        print("3. Exit Portal")

        choice = input("Enter Choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            student_login()
        elif choice == "3":
            print("Program Ended")
            break
        else:
            print("Invalid Choice")    



#========RUN PROGRAM=========

main_menu()

#========REGARDS=========

#==============================================
#       Developed By: Ali Zaman  (CYS-35)
#       Contact: +92 333 9470162
#       Email:alizaman15g@gmail.com
#==============================================