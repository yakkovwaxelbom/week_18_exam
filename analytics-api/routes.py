from fastapi import APIRouter, Depends

from mongo_connection import get_db
from dal import Dal

route = APIRouter(tags=['orders'])

@route.get(path='/alerts-by-border-and-priority', status_code=200)
def alerts_by_border_and_priority(db = Depends(get_db)):
    return Dal(db).alerts_by_border_and_priority()

@route.get(path='/top-urgent-zones', status_code=200)
def top_urgent_zones(db = Depends(get_db)):
    return Dal(db).top_urgent_zones()

@route.get(path='/distance-distribution', status_code=200)
def distance_distribution(db = Depends(get_db)):
    return Dal(db).distance_distribution()

@route.get(path='/low-visibility-high-activity', status_code=200)
def low_visibility_high_activity(db = Depends(get_db)):
    return Dal(db).low_visibility_high_activity()

@route.get(path='/hot-zones', status_code=200)
def hot_zones(db = Depends(get_db)):
    return Dal(db).hot_zones()
