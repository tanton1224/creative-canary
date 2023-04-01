from app.models import db, User, environment, SCHEMA


def seed_users():
    demo = User(
        username='Demo', first_name='Demo', last_name='Lition', email='demo@aa.io', password='password')
    olivia = User(
        username='livvlibb', first_name='Olivia', last_name='Libbey', email='olivia.libbey@gmail.com', password='Ol8395982#', is_admin=True)

    db.session.add(demo)
    db.session.add(olivia)
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
