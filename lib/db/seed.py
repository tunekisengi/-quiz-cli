from .models import Session, Category, Question, init_db

# Create tables
init_db()

# Start a session
session = Session()

# Check if database already has data
if session.query(Category).count() == 0:
    # Create categories
    python_cat = Category(name="Python")
    sql_cat = Category(name="SQL")
    oop_cat = Category(name="OOP")

    session.add_all([python_cat, sql_cat, oop_cat])
    session.commit()

    # Add questions
    questions = [
        Question(prompt="What is a list?", answer="A collection of items", category=python_cat),
        Question(prompt="What does SELECT do in SQL?", answer="Retrieves data from a table", category=sql_cat),
        Question(prompt="What is inheritance in OOP?", answer="A class can inherit from another class", category=oop_cat)
    ]
    session.add_all(questions)
    session.commit()

print("Database seeded successfully!")
