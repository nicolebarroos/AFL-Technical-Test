"""Add contract table

Revision ID: 4332f2d05a0d
Revises: 5096a74139f5
Create Date: 2025-01-27 20:10:28.896601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4332f2d05a0d'
down_revision: Union[str, None] = '5096a74139f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('validity_date', sa.DateTime(), nullable=True),
    sa.Column('signing_date', sa.DateTime(), nullable=True),
    sa.Column('fee', sa.Float(), nullable=True),
    sa.Column('services', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contracts_id'), 'contracts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contracts_id'), table_name='contracts')
    op.drop_table('contracts')
    # ### end Alembic commands ###
