#here import mysql.connector
import sqlite3
import threading
import time

# Global flag to stop the exam when time is up
stop_exam = False

# Function to fetch questions from the database based on exam type and subject
def fetch_questions(exam_type, subject):
    #changes here to mysql.connector.connect ("host":,"user":,"passwd": )
    conn = sqlite3.connect('exam_questions.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, question, option1, option2, option3, option4, answer FROM questions WHERE exam_type=? AND subject=?', (exam_type, subject))
    questions = cursor.fetchall()

    conn.close()
    return questions

# Timer function to countdown exam time and stop when time is up
def countdown_timer(duration):
    global stop_exam
    while duration > 0 and not stop_exam:
        mins, secs = divmod(duration, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f'Time left: {timer}', end="\r")
        time.sleep(1)
        duration -= 1
    
    if duration == 0:
        stop_exam = True
        print("\nTime is up!")

# Exam function with question navigation and timer
def exam_with_navigation(exam_type, subject, duration):
    global stop_exam
    stop_exam = False

    # Fetch the questions from the database
    questions = fetch_questions(exam_type, subject)
    total_questions = len(questions)
    current_question = 0
    answers = {}  # Dictionary to store the user's answers

    # Start the timer in a separate thread
    timer_thread = threading.Thread(target=countdown_timer, args=(duration * 60,))
    timer_thread.start()

    while not stop_exam:
        # Display current question
        question = questions[current_question]
        print(f"\nQuestion {current_question + 1}: {question[1]}")
        print(f"1. {question[2]}")
        print(f"2. {question[3]}")
        print(f"3. {question[4]}")
        print(f"4. {question[5]}")

        # Get user's input for answer or navigation
        action = input("Enter your answer (1-4) or 'n' for next, 'p' for previous, 's' to submit: ")

        # Check if time is up while answering
        if stop_exam:
            print("\nTime's up! Submitting the exam automatically...")
            break

        if action in ['1', '2', '3', '4']:
            answers[question[0]] = action  # Store the answer with the question ID
            print(f"Answer saved for question {current_question + 1}")
        elif action == 'n':
            if current_question < total_questions - 1:
                current_question += 1
            else:
                print("You are at the last question.")
        elif action == 'p':
            if current_question > 0:
                current_question -= 1
            else:
                print("You are at the first question.")
        elif action == 's':
            print("Exam submitted.")
            break
        else:
            print("Invalid input, please try again.")

    # If time's up, wait for the timer thread to end
    timer_thread.join()

    # Calculate the score
    score = 0
    for q_id, answer in answers.items():
        correct_answer = next(q[6] for q in questions if q[0] == q_id)
        if answer == correct_answer:
            score += 1

    print(f"\nYour score: {score}/{total_questions}")

    # Display the results with the correct answers
    print("\nReview your answers:")
    for question in questions:
        q_id = question[0]
        user_answer = answers.get(q_id, None)
        correct_answer = question[6]

        # Display the question and options
        print(f"\nQuestion: {question[1]}")
        print(f"1. {question[2]}")
        print(f"2. {question[3]}")
        print(f"3. {question[4]}")
        print(f"4. {question[5]}")
        if user_answer:
            print(f"Your answer: {user_answer} (Correct answer: {correct_answer})")
            if user_answer == correct_answer:
                print("Result: Correct")
            else:
                print("Result: Incorrect")
        else:
            print(f"You did not answer this question. (Correct answer: {correct_answer})")

# Selection function for choosing the exam and subject
def select():
    x = input("Enter the mode of examination (neet(1)/jee(2)): ")
    y = input("Enter mode of exam (full paper(f)/subject paper(s)): ")

    try:
        if y == "s":
            if x == "1":
                s = input("Choose subject (botany(b)/zoology(z)/physics(p)/chemistry(c)): ")
                if s == "b":
                    return ('neet', 'botany', 30)  # Time in minutes
                elif s == "z":
                    return ('neet', 'zoology', 30)
                elif s == "p":
                    return ('neet', 'physics', 30)
                elif s == "c":
                    return ('neet', 'chemistry', 30)
                else:
                    raise ValueError("Invalid subject selected!")
            elif x == "2":
                s = input("Choose subject (physics(p)/chemistry(c)/maths(m)): ")
                if s == "c":
                    return ('jee', 'chemistry', 30)
                elif s == "m":
                    return ('jee', 'maths', 30)
                elif s == "p":
                    return ('jee', 'physics', 30)
                else:
                    raise ValueError("Invalid subject selected!")
        elif y == "f":
            if x == "1":
                return ('neet', 'full', 180)  # 180 minutes for full paper
            elif x == "2":
                return ('jee', 'full', 180)
            else:
                raise ValueError("Invalid mode of examination selected!")
        else:
            raise ValueError("Invalid mode of exam!")
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Main script execution
top = select()
if top:
    print(f"Selected exam: {top}")
    exam_with_navigation(top[0], top[1], top[2])
