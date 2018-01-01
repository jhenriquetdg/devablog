"""followers

Revision ID: 96fb73f9a58e
Revises: 43070ff7ead7
Create Date: 2017-12-31 16:58:10.856167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96fb73f9a58e'
down_revision = '43070ff7ead7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
