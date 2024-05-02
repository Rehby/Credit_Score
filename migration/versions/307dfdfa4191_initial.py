"""initial

Revision ID: 307dfdfa4191
Revises: 
Create Date: 2024-05-02 16:31:09.582892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '307dfdfa4191'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CreditStatus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Salary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sallary', sa.Integer(), nullable=True),
    sa.Column('clear_sallary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CreditInfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('credit_size', sa.Integer(), nullable=True),
    sa.Column('period', sa.Integer(), nullable=True),
    sa.Column('max_size', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['status'], ['CreditStatus.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PeopleInfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fio', sa.String(), nullable=False),
    sa.Column('active_credit_size', sa.Integer(), nullable=True),
    sa.Column('co_borrower_size', sa.Integer(), nullable=True),
    sa.Column('co_credit_peoples', sa.Integer(), nullable=True),
    sa.Column('poruch', sa.Boolean(), nullable=True),
    sa.Column('children_count', sa.Integer(), nullable=True),
    sa.Column('children_aliment_count', sa.Integer(), nullable=True),
    sa.Column('marriage', sa.Boolean(), nullable=True),
    sa.Column('creditInfo', sa.Integer(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creditInfo'], ['CreditInfo.id'], ),
    sa.ForeignKeyConstraint(['salary'], ['Salary.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PeopleInfo')
    op.drop_table('CreditInfo')
    op.drop_table('Salary')
    op.drop_table('CreditStatus')
    # ### end Alembic commands ###
