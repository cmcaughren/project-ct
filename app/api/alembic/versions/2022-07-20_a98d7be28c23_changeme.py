"""CHANGEME

Revision ID: a98d7be28c23
Revises: b28b9c211ee0
Create Date: 2022-07-20 20:46:58.482077

"""

# revision identifiers, used by Alembic.
revision = 'a98d7be28c23'
down_revision = 'b28b9c211ee0'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from alembic import context


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get("data", None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get("data", None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient_encounters', sa.Column('arrival_date', sa.DateTime(), nullable=True))
    op.add_column('patient_encounters', sa.Column('departure_date', sa.DateTime(), nullable=True))
    op.drop_column('patient_encounters', 'date')
    # ### end Alembic commands ###


def schema_downgrades():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient_encounters', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('patient_encounters', 'departure_date')
    op.drop_column('patient_encounters', 'arrival_date')
    # ### end Alembic commands ###


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass