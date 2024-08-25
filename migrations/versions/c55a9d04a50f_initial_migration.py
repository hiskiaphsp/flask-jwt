"""Initial migration

Revision ID: c55a9d04a50f
Revises: 
Create Date: 2024-08-24 10:49:54.476887

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c55a9d04a50f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=150), nullable=False))
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', mysql.VARCHAR(length=150), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###
