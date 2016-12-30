"""initial migration

Revision ID: 455384bcdb8a
Revises: 9da7f592c30d
Create Date: 2016-12-30 10:25:59.441000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455384bcdb8a'
down_revision = '9da7f592c30d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###