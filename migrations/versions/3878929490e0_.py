"""empty message

Revision ID: 3878929490e0
Revises: fe6ce32bfe67
Create Date: 2024-12-13 13:09:06.279075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3878929490e0'
down_revision = 'fe6ce32bfe67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('transaction_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
        batch_op.alter_column('last_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('last_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
        batch_op.alter_column('transaction_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###
