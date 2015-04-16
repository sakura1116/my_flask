# -*- coding: utf-8 -*-
import unittest
from sqlalchemy import *
from datetime import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine('mysql+pymysql://my_flask:my_flask@localhost/my_flask?charset=utf8')


class Tweets(Base):
    __tablename__ = 'tweets'

    id = Column(BIGINT, primary_key=True)
    status_id = Column(VARCHAR(length=255))
    from_user_id = Column(VARCHAR(length=255))
    text = Column(VARCHAR(length=140))
    created_at = Column(VARCHAR(length=50))
    datetime = Column(DATETIME)


class TestSqlAlchemy(unittest.TestCase):

    def test_main(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # SELECT
        self.assertEqual(0, self.session.query(Tweets).count())

        # INSERT
        tweet = Tweets(
            status_id='251298602096xxxxx1',
            from_user_id='43172xxx1',
            text='さんぷるでーた',
            created_at='Mon, 1 Oct 2012 12:33:50 +0000',
            datetime=datetime.utcnow(),
        )

        # インスタンスを生成しただけでは SQL 文は発行されない
        self.assertEqual(0, self.session.query(Tweets).count())

        # session に追加
        self.session.add(tweet)

        # add で SQL 文は発行されるが COMMIT はされない
        # デフォルトは autocommit=False
        self.assertEqual(1, self.session.query(Tweets).count())

        tweet = Tweets(
            status_id='251298602096xxxxx2',
            from_user_id='43172xxx2',
            text='さんぷるでーた その 2',
            created_at='Mon, 1 Oct 2012 12:33:50 +0000',
            datetime=datetime.utcnow(),
        )
        self.session.add(tweet)

        self.assertEqual(2, self.session.query(Tweets).count())

        # COMMIT を発行して確定
        self.session.commit()

        self.assertEqual(1, self.session.query(Tweets).filter(
            Tweets.from_user_id == '43172xxx2').count())
        self.assertEqual(0, self.session.query(Tweets).filter(
            Tweets.from_user_id == '43172xxx3').count())

        # UPDATE
        for tweet in self.session.query(Tweets).filter(
                Tweets.from_user_id == '43172xxx2'):
            tweet.from_user_id = '43172xxx3'

        self.assertEqual(0, self.session.query(Tweets).filter(
            Tweets.from_user_id == '43172xxx2').count())
        self.assertEqual(1, self.session.query(Tweets).filter(
            Tweets.from_user_id == '43172xxx3').count())

        # DELETE
        for tweet in self.session.query(Tweets).all():
            self.session.delete(tweet)

        self.assertEqual(0, self.session.query(Tweets).count())

        # COMMIT を発行して確定
        self.session.commit()

        # bulk INSERT
        insert_lst = [
            {
                'status_id': '251298602096xxxxx3',
                'from_user_id': '43172xxx3',
                'text': 'さんぷるでーた その 3',
                'created_at': 'Mon, 1 Oct 2012 12:33:50 +0000',
                'datetime': datetime.utcnow(),
            },
            {
                'status_id': '251298602096xxxxx4',
                'from_user_id': '43172xxx4',
                'text': 'さんぷるでーた その 4',
                'created_at': 'Mon, 1 Oct 2012 12:33:50 +0000',
                'datetime': datetime.utcnow(),
            },
        ]

        # 実行(ORMの場合は以下の書き方をする。Core だともっと綺麗に書ける)
        self.session.execute(Tweets().__table__.insert(), insert_lst)

        self.assertEqual(2, self.session.query(Tweets).count())

        # COMMIT しないと ROLLBACK

if __name__ == '__main__':
    unittest.main()