"""empty message

Revision ID: 90d7155db90d
Revises: e4e1488de72c
Create Date: 2024-12-13 11:09:19.620006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d7155db90d'
down_revision = 'e4e1488de72c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_updated', sa.DateTime(), nullable=True))

    with op.batch_alter_table('transaction_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('transaction_type', sa.String(length=50), nullable=True))
        batch_op.create_foreign_key(None, 'transaction', ['transaction_type'], ['transaction_type'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction_item', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('transaction_type')

    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.drop_column('last_updated')

    # ### end Alembic commands ###
