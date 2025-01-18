# List of questions with multiple choices and correct answer
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "choices": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    }
]

# Function to display the quiz and get user input
def run_quiz():
    score = 0
    print("Welcome to the Quiz!\n")
    
    # Loop through each question in the quiz data
    for idx, question_data in enumerate(quiz_data):
        print(f"Q{idx + 1}: {question_data['question']}")
        for choice in question_data["choices"]:
            print(choice)
        
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        # Check if the user's answer is correct
        if user_answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question_data['answer']}\n")
    
    # Display final score
    print(f"Quiz Over! Your final score is: {score}/{len(quiz_data)}")

# Main function to start the quiz
def main():
    run_quiz()

# Run the quiz application
if __name__ == "__main__":
    main()
