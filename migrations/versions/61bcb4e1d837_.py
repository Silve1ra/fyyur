"""empty message

Revision ID: 61bcb4e1d837
Revises: 593f1f2b006d
Create Date: 2021-03-30 17:19:43.685605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61bcb4e1d837'
down_revision = '593f1f2b006d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('venues', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
