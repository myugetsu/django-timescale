from typing import List
from datetime import datetime
from ninja import NinjaAPI, Schema
from sensors import services

api = NinjaAPI()

# to serialize json data we create a schema for the json output
class AvgTempSchema(Schema): #pydantic
  avg_temp: float
  time_group: datetime

class NodeAvgTempSchema(Schema): #pydantic
  node_id: int
  avg_temp: float
  time_group: datetime

class MaxMinTempSchema(Schema): #pydantic
  max_temp: float
  min_temp: float

class NodeMaxMinTempSchema(Schema): #pydantic
  node_id: int
  max_temp: float
  min_temp: float

@api.get('/temps', response=List[AvgTempSchema])
def get_average_temps(request):
  qs = services.get_avg_temp()
  return qs

@api.get('/temps/node', response=List[NodeAvgTempSchema])
def get_average_temps(request):
  qs = services.get_node_avg_temp()
  return qs

@api.get('/temps/maxmin', response=MaxMinTempSchema)
def get_average_temps(request):
  qs = services.get_max_min_temp()
  return qs

@api.get('/temps/nodes/maxmin', response=List[NodeMaxMinTempSchema])
def get_average_temps(request):
  qs = services.get_node_max_min_temp()
  return qs
