import time

# =========QUESTION BANK=========

questions = [
    {
        "id": 1,
        "subject": "Biology",
        "question": "During The Light Reaction Of Photosynthesis, ATP Is Produced Through:",
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
        "question": "The Oxidation Number Of Sulfur In H2SO4 Is:",
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
        "question": "The Escape Velocity From Earth Depends Upon:",
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
        "question": "Who Dissolved The National Assembly In 1977?",
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
        "question": "Which Event Officially Marked The Beginning Of World War I?",
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
        "question": "The Name 'BELLIS PERENNIS' Refers To:",
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
        "question": "Which Loop Repeats Until Condition Becomes False?",
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
        "question": "Which Of The Following Compounds Can Show Geometrical Isomerism?",
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
        "question": "According To Gauss's Law, Electric Field Inside A Uniformly Charged Sphere Varies As:",
        "choices": {
            "A": "1/r^2",
            "B": "r",
            "C": "Constant",
            "D": "Zero Everywhere"
        },
        "answer": "B"
    }
]

# =========CONSTANTS=========
CORRECT_MARKS = 4
WRONG_MARKS   = -1
SKIP_MARKS    = 0

# =========RESULT STORAGE=========
all_results = []

# =========CALCULATE RESULT=========
def calculate_result(name, roll_no, answers):
    correct = wrong = skipped = 0
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
            "question":       questions[idx]["question"],
            "student_answer": student_answer,
            "correct_answer": correct_answer,
            "status":         status
        })

    score        = (correct * CORRECT_MARKS) + (wrong * WRONG_MARKS)
    total_marks  = len(questions) * CORRECT_MARKS
    percentage   = (score / total_marks) * 100 if total_marks > 0 else 0

    if percentage >= 80:
        grade = "EXCELLENT"
    elif percentage >= 65:
        grade = "GOOD"
    elif percentage >= 50:
        grade = "AVERAGE"
    else:
        grade = "BELOW AVERAGE"

    result = {
        "name":       name,
        "roll_no":    roll_no,
        "correct":    correct,
        "wrong":      wrong,
        "skipped":    skipped,
        "score":      score,
        "percentage": round(percentage, 2),
        "grade":      grade,
        "time":       time.strftime("%d-%m-%Y %H:%M:%S"),
        "review":     review
    }

    all_results.append(result)
    return result

# ==============================================
#   Developed By: Ali Zaman  (CYS-35)
#   Contact: +92 333 9470162
#   Email: alizaman15g@gmail.com
# ==============================================
