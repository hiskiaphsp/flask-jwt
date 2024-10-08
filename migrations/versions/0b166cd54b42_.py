"""empty message

Revision ID: 0b166cd54b42
Revises: c55a9d04a50f
Create Date: 2024-08-25 07:38:40.046041

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0b166cd54b42'
down_revision = 'c55a9d04a50f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###
