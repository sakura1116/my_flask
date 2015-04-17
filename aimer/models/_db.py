# -*- coding: utf-8 -*-

from flask_sqlalchemy import BaseQuery
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, exc, Session

engine = create_engine('mysql+pymysql://my_flask:my_flask@localhost/my_flask?charset=utf8')





