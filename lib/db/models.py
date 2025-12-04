from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Database engine
engine = create_engine("sqlite:///quiz.db")

# Base class
Base = declarative_base()

# Session
Session = sessionmaker(bind=engine)
session = Session()

# ============================
#  CATEGORY MODEL
# ============================
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    questions = relationship("Question", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"

# ============================
#  QUESTION MODEL
# ============================
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    prompt = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="questions")

    def __repr__(self):
        return f"<Question {self.prompt}>"

# ============================
#  QUIZ ATTEMPT MODEL
# ============================
class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    score = Column(Integer)
    total = Column(Integer)
    taken_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Attempt {self.category_name}: {self.score}/{self.total}>"

# Create tables if they don't exist
def init_db():
    Base.metadata.create_all(engine)
