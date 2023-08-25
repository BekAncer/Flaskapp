"""create a sneakers db

Revision ID: 38d9ab89d477
Revises: 
Create Date: 2023-08-17 00:28:38.688348

"""
from alembic import op
import sqlalchemy as db
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '38d9ab89d477'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'sneaker',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('name', db.String(50), unique=True, nullable=False),
        db.Column('price', db.Integer, nullable=False),
        db.Column('imgsrc', db.String(100), nullable=False),
        db.Column('date', db.DateTime, default=datetime.utcnow())
    )


def downgrade() -> None:
    op.drop_table(sneaker)
