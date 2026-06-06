import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer

# Import logic from ecat.py
from ecat import questions, all_results, calculate_result, CORRECT_MARKS

# 
#  MAIN APPLICATION CLASS
# 
class ECATApp(QtWidgets.QMainWindow):

    # ── Page for outer stackedWidget ──
    PAGE_MAIN         = 0   # main
    PAGE_LOGIN        = 1   # login
    PAGE_STUDENT_MENU = 2   # student menu
    PAGE_EXAM         = 3   # exam
    PAGE_ADMIN_MENU   = 4   # admin menu  (inner stackedWidget_2)

    # ─ Sub-page for inner stackedWidget_2 ─
    ADMIN_HOME        = 0
    ADMIN_VIEW_QS     = 1
    ADMIN_ADD_Q       = 2
    ADMIN_DELETE_Q    = 3
    ADMIN_ALL_RESULTS = 4
    ADMIN_DETAIL_RES  = 5
    ADMIN_Q_STATS     = 6
    ADMIN_CLASS_STATS = 7

    def __init__(self):
        super().__init__()
        uic.loadUi("Ecat.ui", self)
        self.setWindowTitle("ECAT Exam Portal")

        # ── State ──
        self.current_user_type  = None
        self.student_name       = ""
        self.student_roll       = ""
        self.admin_attempts     = 3
        self.student_attempts   = 3
        self.exam_answers       = {}
        self.current_q_index    = 0
        self.exam_seconds_left  = 20 * 60

        # ── Timer ──
        self.exam_timer = QTimer()
        self.exam_timer.timeout.connect(self.update_timer)

        self._connect_signals()

    # 
    #  CONNECT ALL BUTTONS TO FUNCTIONS
    # 
    def _connect_signals(self):
        # Main menu
        self.btn_admin.clicked.connect(self.go_admin_login)
        self.btn_student.clicked.connect(self.go_student_login)

        # Login page
        self.btn_login.clicked.connect(self.handle_login)
        self.btn_back.clicked.connect(self.go_main)

        # Student menu
        self.btn_start_exam.clicked.connect(self.start_exam)
        self.btn_view_rules.clicked.connect(self.show_rules)
        self.btn_student_logout.clicked.connect(self.go_main)

        # Exam page
        self.btn_next.clicked.connect(self.next_question)
        self.btn_skip.clicked.connect(self.skip_question)
        self.btn_submit.clicked.connect(self.submit_exam)

        # Admin sidebar buttons
        self.btn_view_questions.clicked.connect(self.show_view_questions)
        self.btn_add_question.clicked.connect(self.show_add_question)
        self.btn_delete_question.clicked.connect(self.show_delete_question)
        self.btn_question_statistics.clicked.connect(self.show_q_statistics)
        self.btn_view_all_results.clicked.connect(self.show_all_results)
        self.btn_view_detailed_result.clicked.connect(self.show_detailed_result_page)
        self.btn_class_statistics.clicked.connect(self.show_class_stats)
        self.btn_logout.clicked.connect(self.go_main)

        # Admin content buttons
        self.btn_save.clicked.connect(self.save_question)
        self.btn_delete.clicked.connect(self.delete_question)
        self.btn_search.clicked.connect(self.search_detailed_result)

    # 
    #  NAVIGATION
    # 
    def go_main(self):
        """Stop any exam, reset attempts, go to main menu."""
        self.exam_timer.stop()
        self.admin_attempts   = 3
        self.student_attempts = 3
        self.input_username.clear()
        self.input_password.clear()
        self.input_name.clear()
        self.input_roll_no.clear()
        self.label_attempts.setText("Attempts Remaining: 3")
        self.stackedWidget.setCurrentIndex(self.PAGE_MAIN)

    def go_admin_login(self):
        self.current_user_type = "admin"
        self.label_login_title.setText("ADMIN LOGIN")
        # Hide student fields
        self.label_name.hide()
        self.input_name.hide()
        self.label_roll.hide()
        self.input_roll_no.hide()
        self.stackedWidget.setCurrentIndex(self.PAGE_LOGIN)

    def go_student_login(self):
        self.current_user_type = "student"
        self.label_login_title.setText("STUDENT LOGIN")
        # Show student-only fields
        self.label_name.show()
        self.input_name.show()
        self.label_roll.show()
        self.input_roll_no.show()
        self.stackedWidget.setCurrentIndex(self.PAGE_LOGIN)

    # 
    #  LOGIN HANDLER
    # 
    def handle_login(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        if self.current_user_type == "admin":
            if username == "ecat_admin" and password == "ecat@2026":
                self.admin_attempts = 3
                self.input_username.clear()
                self.input_password.clear()
                self.label_attempts.setText("Attempts Remaining: 3")
                self.stackedWidget_2.setCurrentIndex(self.ADMIN_HOME)
                self.stackedWidget.setCurrentIndex(self.PAGE_ADMIN_MENU)
            else:
                self.admin_attempts -= 1
                if self.admin_attempts <= 0:
                    QtWidgets.QMessageBox.critical(self, "Account Locked",
                        "Too many failed attempts. Account locked.")
                    self.go_main()
                else:
                    self.label_attempts.setText(f"Attempts Remaining: {self.admin_attempts}")
                    QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

        else:  # student
            if username == "student" and password == "student123":
                name    = self.input_name.text().strip()
                roll_no = self.input_roll_no.text().strip()
                if not name or not roll_no:
                    QtWidgets.QMessageBox.warning(self, "Missing Info",
                        "Please enter your Full Name and Roll Number.")
                    return
                self.student_name = name
                self.student_roll = roll_no
                self.student_attempts = 3
                self.label_welcome.setText(f"Welcome, {self.student_name}!")
                self.input_username.clear()
                self.input_password.clear()
                self.label_attempts.setText("Attempts Remaining: 3")
                self.stackedWidget.setCurrentIndex(self.PAGE_STUDENT_MENU)
            else:
                self.student_attempts -= 1
                if self.student_attempts <= 0:
                    QtWidgets.QMessageBox.critical(self, "Account Locked",
                        "Too many failed attempts. Account locked.")
                    self.go_main()
                else:
                    self.label_attempts.setText(f"Attempts Remaining: {self.student_attempts}")
                    QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    # 
    #  EXAM RULES
    # 
    def show_rules(self):
        QtWidgets.QMessageBox.information(self, "Exam Rules",
            "ECAT EXAM RULES\n\n"
            "1.  The exam has 10 multiple-choice questions.\n"
            "2.  Select A, B, C or D, then click Next.\n"
            "3.  Click Skip to skip a question (no penalty).\n"
            "4.  Correct answer  →  +4 marks\n"
            "5.  Wrong answer    →  -1 mark\n"
            "6.  Skipped         →   0 marks\n"
            "7.  Click Submit on the last question to finish.\n"
            "8.  Total time: 20 minutes.\n"
            "9.  Exam auto-submits when time runs out."
        )

    # 
    #  EXAM: START / LOAD / NAVIGATE
    # 
    def start_exam(self):
        if len(questions) == 0:
            QtWidgets.QMessageBox.warning(self, "No Questions",
                "There are no questions in the question bank.")
            return
        self.exam_answers      = {}
        self.current_q_index   = 0
        self.exam_seconds_left = 20 * 60
        self.stackedWidget.setCurrentIndex(self.PAGE_EXAM)
        self.load_question(0)
        self.exam_timer.start(1000)

    def load_question(self, idx):
        q = questions[idx]
        total = len(questions)

        self.label_q_counter.setText(f"Question {idx + 1} of {total}")
        self.label_subject.setText(q["subject"])
        self.label_question.setText(q["question"])
        self.radio_a.setText("A:  " + q["choices"]["A"])
        self.radio_b.setText("B:  " + q["choices"]["B"])
        self.radio_c.setText("C:  " + q["choices"]["C"])
        self.radio_d.setText("D:  " + q["choices"]["D"])

        # Uncheck all radio buttons
        for rb in [self.radio_a, self.radio_b, self.radio_c, self.radio_d]:
            rb.setAutoExclusive(False)
            rb.setChecked(False)
            rb.setAutoExclusive(True)

        # Restore previously saved answer
        saved = self.exam_answers.get(idx)
        if saved and saved != "S":
            mapping = {"A": self.radio_a, "B": self.radio_b,
                       "C": self.radio_c, "D": self.radio_d}
            if saved in mapping:
                mapping[saved].setChecked(True)

        # Show Next on all questions;show Submit only on last
        is_last = (idx == total - 1)
        self.btn_next.setVisible(not is_last)
        self.btn_submit.setVisible(is_last)

    def get_selected_answer(self):
        if self.radio_a.isChecked(): return "A"
        if self.radio_b.isChecked(): return "B"
        if self.radio_c.isChecked(): return "C"
        if self.radio_d.isChecked(): return "D"
        return None

    def next_question(self):
        ans = self.get_selected_answer()
        if ans is None:
            QtWidgets.QMessageBox.warning(self, "No Selection",
                "Please select an answer or click Skip.")
            return
        self.exam_answers[self.current_q_index] = ans
        self.current_q_index += 1
        self.load_question(self.current_q_index)

    def skip_question(self):
        self.exam_answers[self.current_q_index] = "S"
        if self.current_q_index < len(questions) - 1:
            self.current_q_index += 1
            self.load_question(self.current_q_index)
        else:
            self.finish_exam()

    def submit_exam(self):
        ans = self.get_selected_answer()
        self.exam_answers[self.current_q_index] = ans if ans else "S"
        self.finish_exam()

    def finish_exam(self):
        self.exam_timer.stop()
        result = calculate_result(self.student_name, self.student_roll, self.exam_answers)
        total  = len(questions) * CORRECT_MARKS
        QtWidgets.QMessageBox.information(self, "Exam Complete — Result",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  Name    : {result['name']}\n"
            f"  Roll No : {result['roll_no']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  Correct : {result['correct']}\n"
            f"  Wrong   : {result['wrong']}\n"
            f"  Skipped : {result['skipped']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  Score   : {result['score']} / {total}\n"
            f"  Percent : {result['percentage']}%\n"
            f"  Grade   : {result['grade']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        self.stackedWidget.setCurrentIndex(self.PAGE_STUDENT_MENU)

    def update_timer(self):
        self.exam_seconds_left -= 1
        mins = self.exam_seconds_left // 60
        secs = self.exam_seconds_left % 60
        self.label_timer.setText(f"{mins:02}:{secs:02}")
        # Turn timer red in last 5 minutes
        if self.exam_seconds_left <= 300:
            self.label_timer.setStyleSheet(
                "QLabel { color: #ef4444; font-size: 22px; font-weight: bold; background-color: transparent; }")
        if self.exam_seconds_left <= 0:
            QtWidgets.QMessageBox.information(self, "Time Up", "Time is up! Your exam is being submitted.")
            self.finish_exam()

    # 
    #  ADMIN: VIEW QUESTIONS
    # 
    def show_view_questions(self):
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_VIEW_QS)
        if not questions:
            self.output_view_questions.setPlainText("No questions in the bank.")
            return
        lines = []
        for q in questions:
            lines.append(f"ID: {q['id']}   Subject: {q['subject']}")
            lines.append(f"Q:  {q['question']}")
            for k, v in q["choices"].items():
                lines.append(f"    {k}: {v}")
            lines.append(f"Ans: {q['answer']}")
            lines.append("─" * 60)
        self.output_view_questions.setPlainText("\n".join(lines))

    # 
    #  ADMIN: ADD QUESTION
    # 
    def show_add_question(self):
        for field in [self.input_subject, self.input_question,
                      self.input_option_a, self.input_option_b,
                      self.input_option_c, self.input_option_d,
                      self.input_correct_answer]:
            field.clear()
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_ADD_Q)

    def save_question(self):
        subject  = self.input_subject.text().strip()
        question = self.input_question.text().strip()
        opt_a    = self.input_option_a.text().strip()
        opt_b    = self.input_option_b.text().strip()
        opt_c    = self.input_option_c.text().strip()
        opt_d    = self.input_option_d.text().strip()
        answer   = self.input_correct_answer.text().strip().upper()

        if not all([subject, question, opt_a, opt_b, opt_c, opt_d, answer]):
            QtWidgets.QMessageBox.warning(self, "Incomplete", "Please fill in ALL fields.")
            return
        if answer not in ("A", "B", "C", "D"):
            QtWidgets.QMessageBox.warning(self, "Invalid Answer",
                "Correct answer must be exactly A, B, C, or D.")
            return

        questions.append({
            "id":      len(questions) + 1,
            "subject": subject,
            "question": question,
            "choices": {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d},
            "answer":  answer
        })
        QtWidgets.QMessageBox.information(self, "Saved",
            f"Question #{len(questions)} added successfully!")
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_HOME)

    # 
    #  ADMIN: DELETE QUESTION
    # 
    def show_delete_question(self):
        self.input_enter_question_id.clear()
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_DELETE_Q)

    def delete_question(self):
        text = self.input_enter_question_id.text().strip()
        if not text.isdigit():
            QtWidgets.QMessageBox.warning(self, "Invalid Input",
                "Please enter a valid numeric Question ID.")
            return
        qid = int(text)
        for i, q in enumerate(questions):
            if q["id"] == qid:
                questions.pop(i)
                QtWidgets.QMessageBox.information(self, "Deleted",
                    f"Question ID {qid} was deleted.")
                self.stackedWidget_2.setCurrentIndex(self.ADMIN_HOME)
                return
        QtWidgets.QMessageBox.warning(self, "Not Found",
            f"No question found with ID {qid}.")

    # 
    #  ADMIN: QUESTION STATISTICS
    # 
    def show_q_statistics(self):
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_Q_STATS)
        counts = {}
        for q in questions:
            counts[q["subject"]] = counts.get(q["subject"], 0) + 1
        lines = [f"Total Questions: {len(questions)}", "", "Subject Breakdown:", "─" * 40]
        for sub, cnt in counts.items():
            lines.append(f"  {sub:<25} {cnt}")
        self.output_question_statistics.setPlainText("\n".join(lines))

    #
    #  ADMIN: ALL RESULTS
    # 
    def show_all_results(self):
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_ALL_RESULTS)
        if not all_results:
            self.output_all_results.setPlainText("No results yet. Students must complete the exam first.")
            return
        lines = []
        for r in all_results:
            lines.append(f"Name: {r['name']}   Roll: {r['roll_no']}")
            lines.append(f"Score: {r['score']}   Percentage: {r['percentage']}%   Grade: {r['grade']}")
            lines.append(f"Time: {r['time']}")
            lines.append("─" * 60)
        self.output_all_results.setPlainText("\n".join(lines))

    # 
    #  ADMIN: DETAILED RESULT
    # 
    def show_detailed_result_page(self):
        self.input_roll.clear()
        self.output_detailed_result.clear()
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_DETAIL_RES)

    def search_detailed_result(self):
        roll = self.input_roll.text().strip()
        if not roll:
            QtWidgets.QMessageBox.warning(self, "Empty", "Please enter a Roll Number.")
            return
        for r in all_results:
            if r["roll_no"] == roll:
                lines = [
                    f"Name    : {r['name']}",
                    f"Roll No : {r['roll_no']}",
                    f"Score   : {r['score']}   Percentage: {r['percentage']}%   Grade: {r['grade']}",
                    "", "Question-by-Question Review:", "═" * 60
                ]
                for i, rev in enumerate(r["review"], 1):
                    lines.append(f"Q{i}:  {rev['question']}")
                    lines.append(f"     Your Answer : {rev['student_answer']}")
                    lines.append(f"     Correct     : {rev['correct_answer']}")
                    lines.append(f"     Result      : {rev['status']}")
                    lines.append("─" * 60)
                self.output_detailed_result.setPlainText("\n".join(lines))
                return
        self.output_detailed_result.setPlainText(
            f"No result found for Roll No: {roll}\n\n"
            "Make sure the student has completed the exam.")

    # 
    #  ADMIN: CLASS STATISTICS
    # 
    def show_class_stats(self):
        self.stackedWidget_2.setCurrentIndex(self.ADMIN_CLASS_STATS)
        if not all_results:
            self.output_class_satistics.setPlainText("No results yet.")
            return
        scores  = [r["score"] for r in all_results]
        pass_c  = sum(1 for r in all_results if r["percentage"] >= 50)
        fail_c  = len(all_results) - pass_c
        grades  = {"EXCELLENT": 0, "GOOD": 0, "AVERAGE": 0, "BELOW AVERAGE": 0}
        for r in all_results:
            grades[r["grade"]] = grades.get(r["grade"], 0) + 1
        lines = [
            f"Total Students  : {len(all_results)}",
            f"Highest Score   : {max(scores)}",
            f"Lowest Score    : {min(scores)}",
            f"Average Score   : {round(sum(scores)/len(scores), 2)}",
            "",
            f"Passed          : {pass_c}",
            f"Failed          : {fail_c}",
            "", "Grade Distribution:", "─" * 40
        ]
        for g, c in grades.items():
            lines.append(f"  {g:<20} {c}")
        self.output_class_satistics.setPlainText("\n".join(lines))


# 
#  ENTRY POINT
# 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ECATApp()
    window.show()
    sys.exit(app.exec_())

# ==============================================
#   Developed By: Ali Zaman  (CYS-35)
#   Contact: +92 333 9470162
#   Email: alizaman15g@gmail.com
# ==============================================
