from app.models import db, Lesson, environment, SCHEMA
from datetime import date, time

def seed_lessons():
    demo = Lesson(
        client_id=1, date=date(2023, 12, 24), start_time=time(14,30), end_time=time(16,30), client_name=('The Best Student'))
    demo1 = Lesson(
        client_id=1, date=date(2023, 12, 24), start_time=time(9,30), end_time=time(11,30), client_name=('The 2nd Best Student'))
    demo2 = Lesson(
        client_id=1, date=date(2023, 12, 24), start_time=time(11,30), end_time=time(13,30), client_name=('The 3rd Best Student'))

    db.session.add(demo)
    db.session.add(demo1)
    db.session.add(demo2)
    db.session.commit()


def undo_lessons():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
