from .db import db, environment, SCHEMA, add_prefix_for_prod

class Event(db.Model):
  __tablename__ = 'events'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date, nullable=False)
  time = db.Column(db.Time, nullable=False)
  event_name = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
  location_name = db.Column(db.String(120), nullable=False)
  location_address = db.Column(db.String(255), nullable=False)
  location_city = db.Column(db.String(120), nullable=False)
  location_state = db.Column(db.String(2), nullable=False)
  location_zip = db.Column(db.String(10), nullable=False)
  ticket_price = db.Column(db.Integer, nullable=False)
  max_tickets = db.Column(db.Integer, nullable=False)

  attendees = db.relationship('User', back_populates='events')

  def to_dict(self):
    return {
            'id': self.id,
            'date,': self.date,
            'time': self.time,
            'event_name,': self.event_name,
            'location_name,': self.location_name,
            'location_address,': self.location_address,
            'location_city,': self.location_city,
            'location_state,': self.location_state,
            'location_zip,': self.location_zip,
            'ticket_price,': self.ticket_price,
            'max_tickets,': self.max_tickets,
            'client,': self.client,
            'attendees': self.attendees,
        }
