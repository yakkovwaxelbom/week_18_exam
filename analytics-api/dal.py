from redis_connection import RedisCashing

class Dal:
    def __init__(self, db):
        self._db = db


    @RedisCashing(expire=3600)
    def alerts_by_border_and_priority(self):
        pipeline = [{
                    "$group": {
                        "_id": {
                            "border": "$border",
                            "priority": "$priority",
                            },
                  "alerts_count": {"$sum": 1 }}},
                  {"$project": 
                    {"_id": 0, 
                     "border": "$_id.border", 
                     "priority": "$_id.priority", 
                     "alerts_count": 1}}]
        
        return list(self._db.alert.aggregate(pipeline))

    @RedisCashing(expire=3600)
    def top_urgent_zones(self):
        pipeline = [
            {"$match": {'priority': 'urgent'}},
            {"$group": {"_id": "$zone", "totalAlerts": {"$sum": 1}}},
            {"$project": {"_id": 0, "zone": "$_id", "totalAlerts": 1}},
            {"$sort": {"totalCuisine": -1}},
            {"$limit": 5}
        ]

        return list(self._db.alert.aggregate(pipeline))
    
    @RedisCashing(expire=3600)
    def distance_distribution(self):
        pipeline = [{"$bucket": {
                            "groupBy": "$distance_from_fence_m",
                            "boundaries": [1, 300, 800, 1500],
                            "default": "indefinite",
                            "output": {"count": { "$sum": 1 }}}
                        }
                    ]
        return list(self._db.alert.aggregate(pipeline))

    @RedisCashing(expire=3600)
    def low_visibility_high_activity(self):
        pass

    @RedisCashing(expire=3600)
    def hot_zones(self):
        pass