from .db.models import Session, Category, Question, QuizAttempt
from datetime import datetime

session = Session()

def list_categories():
    categories = session.query(Category).all()
    print("\nCategories:")
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat.name}")
    return categories

def select_category(categories):
    choice = int(input("\nChoose a category number: "))
    return categories[choice - 1]

def run_quiz(category):
    questions = session.query(Question).filter_by(category_id=category.id).all()
    score = 0
    total = len(questions)

    for q in questions:
        print(f"\nQuestion: {q.prompt}")
        answer = input("Answer: ").strip()
        if answer.lower() == q.answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q.answer}")

    # Save attempt
    attempt = QuizAttempt(category_name=category.name, score=score, total=total, taken_at=datetime.utcnow())
    session.add(attempt)
    session.commit()

    print(f"\nYou scored {score}/{total} in {category.name} category!")

def show_attempts():
    attempts = session.query(QuizAttempt).all()
    if attempts:
        print("\nPrevious attempts:")
        for a in attempts:
            print(f"{a.taken_at.strftime('%Y-%m-%d %H:%M:%S')} - {a.category_name}: {a.score}/{a.total}")
    else:
        print("No attempts yet.")

def main():
    print("=== Welcome to QuizMaster CLI ===")
    while True:
        print("\n1. Take a Quiz\n2. View Past Attempts\n3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            categories = list_categories()
            category = select_category(categories)
            run_quiz(category)
        elif choice == "2":
            show_attempts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
