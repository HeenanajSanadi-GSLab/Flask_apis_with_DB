"""empty message

Revision ID: 9b65c635e001
Revises: 
Create Date: 2018-07-02 15:01:10.103000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b65c635e001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('alias', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_pkey'),
    sa.UniqueConstraint('email', name=u'user_email_key'),
    sa.UniqueConstraint('username', name=u'user_username_key')
    )
    op.drop_table('comments')
    op.drop_table('categories')
    # ### end Alembic commands ###