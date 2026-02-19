import json

from priority_logic import PriorityLogic
from redis_connection import RedisMsgQueue

TTL = 3600

def main():

    RedisMsgQueue.connect()

    with open('data/border_alerts.json') as f:

        data = json.load(f)

    for alert in data:
        priority = PriorityLogic.get_priority(alert)
        RedisMsgQueue.push_queue(priority, TTL, alert)


if __name__ == '__main__':
    main()