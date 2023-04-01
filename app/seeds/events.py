from app.models import db, Event, environment, SCHEMA
from datetime import date, time

def seed_events():
    demo = Event(
        date=date(2023, 12, 24),
        time=time(14,30),
        event_name=('The Best Event'),
        location_name="Buzzed Viking",
        location_address="123 Street Avenue",
        location_city="Charlotte",
        location_state="NC",
        location_zip="28269",
        ticket_price=25,
        max_tickets=30)
    demo1 = Event(
        date=date(2023, 12, 18),
        time=time(9,30),
        event_name=('The 2nd Best Event'),
        location_name="Buzzed Viking",
        location_address="123 Street Avenue",
        location_city="Charlotte",
        location_state="NC",
        location_zip="28269",
        ticket_price=25,
        max_tickets=30)
    demo2 = Event(
        date=date(2023, 12, 12),
        time=time(11,30),
        event_name=('The 3rd Best Event'),
        location_name="Buzzed Viking",
        location_address="123 Street Avenue",
        location_city="Charlotte",
        location_state="NC",
        location_zip="28269",
        ticket_price=25,
        max_tickets=30)

    db.session.add(demo)
    db.session.add(demo1)
    db.session.add(demo2)
    db.session.commit()


def undo_events():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
