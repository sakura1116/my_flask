# -*- coding: utf-8 -*-
from ._base import *

class Tweets(Base):
    __tablename__ = 'tweets'

    id = Column(BIGINT, primary_key=True,autoincrement=True)
    status_id = Column(VARCHAR(length=255))
    from_user_id = Column(VARCHAR(length=255))
    text = Column(VARCHAR(length=140))
    created_at = Column(VARCHAR(length=50))
    datetime = Column(DATETIME)