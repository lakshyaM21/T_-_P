'''
NAME- LAKSHYA MANSHARAMANI
ENROLMENT NO.- 0157AL231117
BATCH- CSE AIML (5TH SEM)
(TNP-(MTF)) - 10:30 A.M.
'''

import json
import csv
import os
import random
from datetime import datetime

USERS_FILE = 'users.json'
SCORES_FILE = 'scores.csv'
QUESTION_FILES = {
    'DSA': 'questions_DSA.json',
    'DBMS': 'questions_DBMS.json',
    'PYTHON': 'questions_PYTHON.json'
}

logged_user = ''
logged = False
is_admin = False
users = {}

def load_users():
    global users
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}
    else:
        users = {}
        users['admin'] = {
            'password': 'admin123',
            'name': 'Administrator',
            'email': '',
            'branch': '',
            'year': '',
            'contact': '',
            'enrollment': '0000'
        }
        save_users()

def save_users():
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def ensure_scores_file():
    if not os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['enrollment', 'username', 'category', 'score', 'total', 'datetime'])

def load_questions(category):
    fname = QUESTION_FILES.get(category)
    if not fname or not os.path.exists(fname):
        return []
    with open(fname, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_questions(category, question_list):
    fname = QUESTION_FILES.get(category)
    if not fname:
        return
    with open(fname, 'w') as f:
        json.dump(question_list, f, indent=2)

def register():
    global users
    print("\n-- Registration --")
    username = input("Enter your username: ").strip()
    if username in users:
        print("This username already exists.")
        return
    password = input("Enter a strong password: ").strip()
    name = input("Full name: ").strip()
    email = input("Email: ").strip()
    branch = input("Branch: ").strip()
    year = input("Year: ").strip()
    contact = input("Contact number: ").strip()
    enrollment = input("Enrollment number: ").strip()
    users[username] = {
        'password': password,
        'name': name,
        'email': email,
        'branch': branch,
        'year': year,
        'contact': contact,
        'enrollment': enrollment
    }
    save_users()
    print(f"Registration successful. Your username is {username}.")

def login():
    global logged, logged_user, is_admin
    if logged:
        print("You are already logged in.")
        return
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    user = users.get(username)
    if user and user.get('password') == password:
        logged = True
        logged_user = username
        is_admin = (username == 'admin')
        print(f"Successfully logged in as {username}.")
    else:
        print("Invalid username or password.")

def logout():
    global logged, logged_user, is_admin
    if logged:
        logged = False
        logged_user = ''
        is_admin = False
        print("You are officially logged out.")
    else:
        print("Already logged out.")

def show_profile():
    if not logged:
        print("You are not logged in yet. Please login first.")
        return
    profile = users.get(logged_user, {})
    print("\n-- Profile --")
    print(f"Username   : {logged_user}")
    print(f"Name       : {profile.get('name','')}")
    print(f"Email      : {profile.get('email','')}")
    print(f"Branch     : {profile.get('branch','')}")
    print(f"Year       : {profile.get('year','')}")
    print(f"Contact    : {profile.get('contact','')}")
    print(f"Enrollment : {profile.get('enrollment','')}")
    print(f"Role       : {'Admin' if is_admin else 'User'}")

def update_profile():
    if not logged:
        print("You are not logged in yet. Please login first.")
        return
    profile = users.get(logged_user)
    print("\n-- Update Profile (leave blank to keep current) --")
    new_name = input(f"Name [{profile.get('name','')}]: ").strip()
    new_email = input(f"Email [{profile.get('email','')}]: ").strip()
    new_branch = input(f"Branch [{profile.get('branch','')}]: ").strip()
    new_year = input(f"Year [{profile.get('year','')}]: ").strip()
    new_contact = input(f"Contact [{profile.get('contact','')}]: ").strip()
    new_password = input("New password (leave blank to keep current): ").strip()
    if new_name: profile['name'] = new_name
    if new_email: profile['email'] = new_email
    if new_branch: profile['branch'] = new_branch
    if new_year: profile['year'] = new_year
    if new_contact: profile['contact'] = new_contact
    if new_password: profile['password'] = new_password
    users[logged_user] = profile
    save_users()
    print("Profile updated successfully.")

def attempt_quiz():
    if not logged:
        print("Please login before attempting a quiz.")
        return
    print("\n-- Attempt Quiz --")
    print("Categories:")
    for i, cat in enumerate(QUESTION_FILES.keys(), start=1):
        print(f"{i}. {cat}")
    choice = input("Select category number: ").strip()
    try:
        choice_idx = int(choice) - 1
        category = list(QUESTION_FILES.keys())[choice_idx]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    questions = load_questions(category)
    if not questions:
        print(f"No questions found for {category}. Contact admin.")
        return
    max_pick = min(10, len(questions))
    num_to_ask = max(5, max_pick) if max_pick >= 5 else max_pick
    selected = random.sample(questions, num_to_ask)
    random.shuffle(selected)
    score = 0
    total = len(selected)
    print(f"\nStarting {category} quiz: {total} questions.\n")
    for idx, q in enumerate(selected, start=1):
        print(f"Q{idx}. {q['question']}")
        options = q['options']
        letters = ['A','B','C','D','E','F']
        for i,opt in enumerate(options):
            print(f"   {letters[i]}. {opt}")
        ans = input("Your answer (A/B/C/...): ").strip().upper()
        chosen_index = None
        if ans in letters[:len(options)]:
            chosen_index = letters.index(ans)
        else:
            print("Invalid option — counted as incorrect.")
        correct_index = q.get('answer_index')
        if chosen_index is not None and chosen_index == correct_index:
            print("Correct!\n")
            score += 1
        else:
            correct_letter = letters[correct_index] if isinstance(correct_index,int) and correct_index < len(letters) else '?'
            print(f"Incorrect. Correct answer: {correct_letter}. {options[correct_index]}\n")
    print(f"Quiz finished. You scored {score}/{total}.\n")
    enrollment = users[logged_user].get('enrollment','')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ensure_scores_file()
    with open(SCORES_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([enrollment, logged_user, category, score, total, now])
    print("Your result has been recorded, plz check it in view score.")

def view_my_scores():
    if not logged:
        print("Please login to view your scores.")
        return
    ensure_scores_file()
    print(f"\n-- Scores for {logged_user} --")
    found = False
    with open(SCORES_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['username'] == logged_user:
                found = True
                print(f"{row['datetime']} | {row['category']} | {row['score']}/{row['total']}")
    if not found:
        print("No scores recorded yet.")

def admin_menu():
    if not logged or not is_admin:
        print("Admin access required.")
        return
    while True:
        print("\n-- Admin Menu --")
        print("1. Add question")
        print("2. View questions")
        print("3. Delete question")
        print("4. Back to main menu")
        choice = input("Select option: ").strip()
        if choice == '1':
            admin_add_question()
        elif choice == '2':
            admin_view_questions()
        elif choice == '3':
            admin_delete_question()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

def admin_add_question():
    print("\nAdd question to which category?")
    for i, cat in enumerate(QUESTION_FILES.keys(), start=1):
        print(f"{i}. {cat}")
    try:
        choice = int(input("Category number: ").strip()) - 1
        category = list(QUESTION_FILES.keys())[choice]
    except:
        print("Invalid selection.")
        return
    qtext = input("Enter question text: ").strip()
    options = []
    print("Enter options one by one (blank to stop):")
    while True:
        opt = input(f"Option {len(options)+1}: ").strip()
        if opt == '':
            break
        options.append(opt)
    if len(options) < 2:
        print("Need at least two options.")
        return
    for i,opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    try:
        correct_num = int(input("Enter correct option number: ").strip())
        correct_index = correct_num - 1
        if correct_index < 0 or correct_index >= len(options):
            raise ValueError()
    except:
        print("Invalid correct option.")
        return
    new_q = {
        'question': qtext,
        'options': options,
        'answer_index': correct_index
    }
    qs = load_questions(category)
    qs.append(new_q)
    save_questions(category, qs)
    print("Question added successfully.")

def admin_view_questions():
    print("\nView questions in which category?")
    for i, cat in enumerate(QUESTION_FILES.keys(), start=1):
        print(f"{i}. {cat}")
    try:
        choice = int(input("Category number: ").strip()) - 1
        category = list(QUESTION_FILES.keys())[choice]
    except:
        print("Invalid selection.")
        return
    qs = load_questions(category)
    if not qs:
        print("No questions in this category.")
        return
    for i,q in enumerate(qs, start=1):
        print(f"\n{i}. {q['question']}")
        for idx,opt in enumerate(q['options']):
            mark = '*' if idx == q['answer_index'] else ' '
            print(f"   [{idx+1}] {opt} {mark}")

def admin_delete_question():
    print("\nDelete question from which category?")
    for i, cat in enumerate(QUESTION_FILES.keys(), start=1):
        print(f"{i}. {cat}")
    try:
        choice = int(input("Category number: ").strip()) - 1
        category = list(QUESTION_FILES.keys())[choice]
    except:
        print("Invalid selection.")
        return
    qs = load_questions(category)
    if not qs:
        print("No questions to delete.")
        return
    for i,q in enumerate(qs, start=1):
        print(f"{i}. {q['question']}")
    try:
        to_del = int(input("Enter question number to delete: ").strip()) - 1
        if to_del < 0 or to_del >= len(qs):
            raise ValueError()
    except:
        print("Invalid number.")
        return
    removed = qs.pop(to_del)
    save_questions(category, qs)
    print("Deleted question:", removed['question'])

def terminate():
    print("Exiting program. Goodbye!")
    exit()

def main():
    load_users()
    ensure_scores_file()
    while True:
        print("\n Welcome in LNCT ")
        response = input('''\n
                Choose option:
                1. Registration
                2. Login (user/admin)
                3. Profile
                4. Update profile
                5. Quiz (attempt)
                6. View my scores
                7. Admin menu (admin only)
                8. Logout
                9. Exit

                Select option (1/2/3/4/5/6/7/8/9):   ''').strip()
        if response == '1':
            register()
        elif response == '2':
            login()
        elif response == '3':
            show_profile()
        elif response == '4':
            update_profile()
        elif response == '5':
            attempt_quiz()
        elif response == '6':
            view_my_scores()
        elif response == '7':
            admin_menu()
        elif response == '8':
            logout()
        elif response == '9':
            terminate()
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
