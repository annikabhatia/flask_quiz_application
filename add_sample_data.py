from app import create_app, db
from app.models import Quiz, Question, Choice

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    quiz = Quiz(title="General Knowledge")

    q1 = Question(text="What is the capital of France?", quiz=quiz)
    c1 = Choice(text="Paris", question=q1)
    c2 = Choice(text="London", question=q1)
    c3 = Choice(text="Berlin", question=q1)
    q1.correct_choice_id = 1  # Assuming c1.id will be 1

    q2 = Question(text="Which planet is known as the Red Planet?", quiz=quiz)
    c4 = Choice(text="Earth", question=q2)
    c5 = Choice(text="Mars", question=q2)
    c6 = Choice(text="Jupiter", question=q2)
    q2.correct_choice_id = 5  # Assuming c5.id will be 5

    db.session.add_all([quiz, q1, c1, c2, c3, q2, c4, c5, c6])
    db.session.commit()
