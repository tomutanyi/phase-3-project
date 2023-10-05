"""Add car_name column to Feedback

Revision ID: 1d13bd4193cd
Revises: 
Create Date: 2023-10-05 16:03:29.340773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d13bd4193cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedbacks', sa.Column('car_name', sa.String(), nullable=True))
    op.create_foreign_key(None, 'feedbacks', 'cars', ['car_name'], ['name'])
    op.drop_column('feedbacks', 'car_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedbacks', sa.Column('car_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'feedbacks', 'cars', ['car_id'], ['id'])
    op.drop_column('feedbacks', 'car_name')
    # ### end Alembic commands ###
