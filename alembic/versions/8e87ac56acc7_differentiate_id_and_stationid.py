"""differentiate id and stationid

Revision ID: 8e87ac56acc7
Revises: e0500786dc11
Create Date: 2021-06-16 13:58:53.034818

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '8e87ac56acc7'
down_revision = 'e0500786dc11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('DailyRaw', sa.Column('StationId', sa.Integer(), nullable=False))
    op.alter_column('DailyRaw', 'DayRelHumMin',
               existing_type=sa.FLOAT(precision=53),
               type_=sa.Float(precision=50),
               existing_nullable=True)
    op.add_column('HourlyRaw', sa.Column('StationId', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('HourlyRaw', 'StationId')
    op.alter_column('DailyRaw', 'DayRelHumMin',
               existing_type=sa.Float(precision=50),
               type_=sa.FLOAT(precision=53),
               existing_nullable=True)
    op.drop_column('DailyRaw', 'StationId')
    # ### end Alembic commands ###