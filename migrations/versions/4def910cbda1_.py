"""empty message

Revision ID: 4def910cbda1
Revises: a7e6734bccbe
Create Date: 2024-12-08 01:33:43.427644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4def910cbda1'
down_revision = 'a7e6734bccbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_selling_price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('success', sa.String(length=50), nullable=True))
        batch_op.drop_column('sucess')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sucess', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_column('success')
        batch_op.drop_column('total_selling_price')

    op.create_table('sale',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sale_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('quantity_sold', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('total_price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('profit', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='sale_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='sale_pkey')
    )
    # ### end Alembic commands ###
