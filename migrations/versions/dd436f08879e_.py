"""empty message

Revision ID: dd436f08879e
Revises: c6e887cfe8f5
Create Date: 2024-12-19 13:01:00.367527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd436f08879e'
down_revision = 'c6e887cfe8f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('low_stock', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('low_stock')

    # ### end Alembic commands ###
