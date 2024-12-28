#1.
def educational_chatbot():
    print("Welcome to the University Bot! How can I assist you today?")
    print("1. Check available courses")
    print("2. Check fee structure")
    print("3. Admission process")
    print("4. Contact support")
    print("5. contact you later")
    
    user_input = input("Please choose an option (1-5): ")

    if user_input == "1":
        print("Available courses: \n1. Computer Science\n2. Business Administration\n3. Mechanical Engineering")
    elif user_input == "2":
        print("Fee structure:\n1. BSC Computer Science: $50,000 per semester\n2. BSC AI : $45,000 per semester\n2. Mechanical Engineering: $60,000 per semester")
    elif user_input == "3":
        print("Admission process:\n1. Fill the online application\n2. Submit required documents\n3. Attend the interview")
    elif user_input == "4":
        print("Support contact: \nEmail: support@university.edu\nPhone: +123-456-7890")
    elif user_input == "5":
        print("Contact you later: good bye!!! ")
        exit()
    else:
        print("Invalid option. Please choose a valid option.")
    
educational_chatbot()
print("Do you want to ask further doubts:")
option=input("Y/N")
if option=="Y":
    educational_chatbot()
else:
    print("Thanks for visiting")


#2.
def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 5 + 7?": "12",
        "Which planet is known as the Red Planet?": "Mars",
        "Who wrote 'Hamlet'?": "Shakespeare"
    }

    score = 0
    total_questions = len(questions)

    for question, correct_answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
        print()

    print(f"Quiz finished! Your score is {score}/{total_questions}")





