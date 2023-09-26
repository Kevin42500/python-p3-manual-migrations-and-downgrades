"""Rename 'name' column to 'full_name'

Revision ID: dcfe49487370
Revises: 
Create Date: 2023-09-26 12:59:40.117511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcfe49487370'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade():
    op.alter_column('students', 'full_name', new_column_name='name')



