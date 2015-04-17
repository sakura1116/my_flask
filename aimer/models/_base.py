# -*- coding: utf-8 -*-
import aimer.models._db
import sqlalchemy
import enum
from collections import OrderedDict, namedtuple
from sqlalchemy import MetaData, func, ForeignKeyConstraint
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import object_session
from sqlalchemy.orm.properties import CompositeProperty
from sqlalchemy.types import TypeDecorator
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.types import (
    String,
    Text,
    Boolean,
    BLOB,
    VARCHAR,
    DATETIME,
    BIGINT
)

from sqlalchemy.schema import (
    Column,
    UniqueConstraint,
    ForeignKey,
    Index
)
from sqlalchemy.dialects.mysql import (
    SMALLINT as SmallInteger,
    TINYINT as TinyInteger,
    INTEGER as Integer,
    BIGINT as BigInteger,
    LONGTEXT as LongText,
    MEDIUMBLOB, MEDIUMTEXT,
)
TRUE = True
FALSE = False
NULL = None
