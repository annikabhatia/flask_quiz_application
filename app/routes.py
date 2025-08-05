from flask import Blueprint, jsonify
from .models import Quiz

api = Blueprint('api', __name__)

@api.route('/quizzes', methods=['GET'])
def get_quizzes():
    quizzes = Quiz.query.all()
    return jsonify([{"id": quiz.id, "title": quiz.title} for quiz in quizzes])
