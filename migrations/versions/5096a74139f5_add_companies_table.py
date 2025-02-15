"""Add companies table

Revision ID: 5096a74139f5
Revises: ce35524d2765
Create Date: 2025-01-27 19:10:48.254020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5096a74139f5'
down_revision: Union[str, None] = 'ce35524d2765'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('trade_name', sa.String(), nullable=True),
    sa.Column('legal_name', sa.String(), nullable=True),
    sa.Column('cnpj', sa.String(), nullable=True),
    sa.Column('uf', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companies_cnpj'), 'companies', ['cnpj'], unique=True)
    op.create_index(op.f('ix_companies_id'), 'companies', ['id'], unique=False)
    op.create_index(op.f('ix_companies_nickname'), 'companies', ['nickname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_companies_nickname'), table_name='companies')
    op.drop_index(op.f('ix_companies_id'), table_name='companies')
    op.drop_index(op.f('ix_companies_cnpj'), table_name='companies')
    op.drop_table('companies')
    # ### end Alembic commands ###
