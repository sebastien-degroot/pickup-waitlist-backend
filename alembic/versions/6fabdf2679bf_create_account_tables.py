"""create account tables

Revision ID: 6fabdf2679bf
Revises: 
Create Date: 2022-04-09 13:07:10.601988

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '6fabdf2679bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('check_in',
    sa.Column('check_in_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('waiting', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('check_in_id')
    )
    op.create_table('game',
    sa.Column('game_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('court', sa.Integer(), nullable=True),
    sa.Column('team_one_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('team_two_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('over', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('game_id')
    )
    op.create_table('player',
    sa.Column('player_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('team_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('player_id')
    )
    op.create_table('score',
    sa.Column('score_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('score_id')
    )
    op.create_table('team',
    sa.Column('team_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('team_name', sa.String(), nullable=True),
    sa.Column('court', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('team_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('team')
    op.drop_table('score')
    op.drop_table('player')
    op.drop_table('game')
    op.drop_table('check_in')
    # ### end Alembic commands ###
