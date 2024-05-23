"""empty message

Revision ID: e56197c1e9bb
Revises: d74e54486be4
Create Date: 2023-09-13 15:05:38.002970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e56197c1e9bb'
down_revision: Union[str, None] = 'd74e54486be4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
