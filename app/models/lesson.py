from .db import db, environment, SCHEMA, add_prefix_for_prod

class Lesson(db.Model):
  __tablename__ = 'lessons'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  date = db.Column(db.Date, nullable=False)
  start_time = db.Column(db.Time, nullable=False)
  end_time = db.Column(db.Time, nullable=False)
  client_name = db.Column(db.String(40), nullable=False)
  approved = db.Column(db.Boolean, default=False)

  client = db.relationship('User', back_populates='lessons')


  def to_dict(self):
    return {
          'id': self.id,
          'client': self.client,
          'date,': self.date,
          'start_time,': self.start_time,
          'end_time,': self.end_time,
          'client_name,': self.client_name,
        }
