from aimer.models._db import *
from aimer.models import Tweets
from datetime import datetime

def execute():
    Session = sessionmaker(bind=engine)
    session = Session()
    tweet = Tweets(status_id='111',
       from_user_id='222',
       text='333',
       created_at='444',
       datetime=datetime.utcnow()
    )
    session.add(tweet)
    session.commit()

if __name__ == '__main__':
    execute()

