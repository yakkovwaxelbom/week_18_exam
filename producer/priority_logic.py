from typing import Dict, Any
from enum import Enum

class PriorityLogic:

    class AlertType(str, Enum):
        URGENT = 'urgent'
        NORMAL = 'normal'


    @classmethod
    def get_priority(cls, alert: Dict[str, Any]):
        if alert['people_count'] > 0:
            return cls.AlertType.URGENT.value
        
        if alert['distance_from_fence_m'] <= 50:
            return cls.AlertType.URGENT.value
        
        if alert['people_count'] >= 8:
            return cls.AlertType.URGENT.value
        
        if alert['vehicle_type'].lower() == 'truck':
            return cls.AlertType.URGENT.value
        
        if alert['distance_from_fence_m'] <= 150 and  alert['people_count'] >= 4:
            return cls.AlertType.URGENT.value
        
        if alert['vehicle_type'].lower() == 'jeep' and alert['people_count'] >= 3:
            return cls.AlertType.URGENT.value
        
        return cls.AlertType.NORMAL.value




