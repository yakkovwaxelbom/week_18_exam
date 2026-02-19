from datetime import datetime

from mongo_connection import MongoConnection, get_db
from redis_connection import RedisMsgQueue


URGENT_QUEUE_NAME = 'urgent'
NORMAL_QUEUE_NAME = 'normal'


def main():

    MongoConnection.connect()
    RedisMsgQueue.connect()

    db = get_db()

    while True:
        data = RedisMsgQueue.get_queue(URGENT_QUEUE_NAME, NORMAL_QUEUE_NAME)
        data['time_insertion'] = datetime.now()

        print(data)

        db.alert.insert_one(data)

if __name__ == '__main__':
    main()

