"""Fixed Rater Model

Revision ID: 7ab4964cb91f
Revises: b754913c1716
Create Date: 2025-02-06 16:59:07.240249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ab4964cb91f'
down_revision: Union[str, None] = 'b754913c1716'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('businessunit')
    op.drop_table('rater')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rater',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('total_premium', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('businessunit',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
