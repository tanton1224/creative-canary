"""empty message

Revision ID: e30ce971b3df
Revises: 
Create Date: 2023-03-18 14:31:18.219496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e30ce971b3df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('event_name', sa.String(), nullable=False),
    sa.Column('location_name', sa.String(length=120), nullable=False),
    sa.Column('location_address', sa.String(length=255), nullable=False),
    sa.Column('location_city', sa.String(length=120), nullable=False),
    sa.Column('location_state', sa.String(length=2), nullable=False),
    sa.Column('location_zip', sa.String(length=10), nullable=False),
    sa.Column('ticket_price', sa.Integer(), nullable=False),
    sa.Column('max_tickets', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_name'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.Column('client_name', sa.String(length=40), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lessons')
    op.drop_table('events')
    op.drop_table('users')
    # ### end Alembic commands ###