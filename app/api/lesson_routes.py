from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, User, Lesson
from ..forms import LessonForm

lesson_routes = Blueprint('lessons', __name__)


@lesson_routes.route('/', methods=['GET'])
@login_required
def get_lessons():
  lessons = Lesson.query.all()
  return jsonify({ 'lessons': [lesson.to_dict() for lesson in lessons] })

@lesson_routes.route('/', methods=['POST'])
@login_required
def create_lesson():
  form = LessonForm()

  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    lesson = Lesson(
      client_id = form.data["client_id"],
      date = form.data["date"],
      start_time = form.data["start_time"],
      end_time = form.data["end_time"],
      client_name = form.data["client_name"],
      approved = False,
    )

    db.session.add(lesson)
    db.session.commit()

    return jsonify({'lesson': lesson.to_dict()}), 201
  else:
    return jsonify({'errors': form.errors}), 400


@lesson_routes.route('/<lesson_id>', methods=['PUT'])
@login_required
def edit_lesson(lesson_id):
  if not current_user.is_admin:
    return jsonify({ 'error': 'You do not have permission to edit this lesson'})

  lesson = Lesson.query.get(lesson_id)

  form = LessonForm()

  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    lesson.client_id = form.data["client_id"],
    lesson.date = form.data["date"],
    lesson.start_time = form.data["start_time"],
    lesson.end_time = form.data["end_time"],
    lesson.client_name = form.data["client_name"],
    lesson.approved = form.data["approved"],

    db.session.commit()

    return jsonify({'lesson': lesson}), 200
  else:
    return jsonify({'errors': form.errors}), 400


@lesson_routes.route('/<lesson_id>', methods=['DELETE'])
@login_required
def delete_lesson(lesson_id):
  if not current_user.is_admin:
    return jsonify({ 'error': 'You do not have permission to delete this lesson'})

  lesson = Lesson.query.get(lesson_id)

  if not lesson:
    return jsonify({ 'error': '404: Lesson could not be found'}), 404
