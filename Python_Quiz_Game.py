questions = {
    "Which language are we learning?": "python",
    "Which function finds the largest value?": "max",
    "Which symbol starts a comment in Python?": "#",
    "Which function calculates the length?": "len",
    "Which data type stores key-value pairs?": "dictionary"
}
score = 0
for question, answer in questions.items():
    user_answer = input(question + " ").lower().strip()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer:", answer)
print("\nQUIZ RESULTS")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Score:", round(score / len(questions) * 100), "%")
