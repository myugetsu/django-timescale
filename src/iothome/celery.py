import os

from celery import Celery
from kombu import Queue, Exchange
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iothome.settings")

app = Celery("iothome")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

nodes = [ # you can base this from an env file
  "node-1",
  "node-2",
  "node-3",
]
# usually good practice to Declare your queues
# CELERY_TASK_QUEUES = [
#   Queue("node-1", Exchange("node-1", routing_key="node-1")),
#   Queue("node-2", Exchange("node-2", routing_key="node-2")),
#   Queue("node-3", Exchange("node-3", routing_key="node-3")),
#   Queue("node-4", Exchange("node-4", routing_key="node-4")),
# ]

# CELERY_TASK_QUEUES = []
# for node in nodes:
#   CELERY_TASK_QUEUES.append(
#     Queue(node, Exchange(node, routing_key=node)),
#   )

# app.conf.task_queues = CELERY_TASK_QUEUES

# create a task queue to differenciate the different nodes created by the distributed system
# command: celery -A iothome worker -Q node-1 -l info

# # create an auto beat scheduler to initiate temp check
# CELERY_BEAT_SCHEDULE = {
#   "check-temp": {
#     "task": "sensors.tasks.measure_temp_task",
#     "schedule": 5.0, # every 5 second
#     "options": {"queue": "node-2"} # for manual measure_temp_task.apply_async(queue="node-1") which is the same as options
#   },
#   # "check-temp-2": {
#   #   "task": "sensors.tasks.measure_temp_task",
#   #   "schedule": 5.0 # every 5 second
#   # }
# }

CELERY_TASK_QUEUES = []
CELERY_BEAT_SCHEDULE = {}
for node in nodes:
  CELERY_TASK_QUEUES.append(
    Queue(node, Exchange(node, routing_key=node)),
  )
  key = f"check-temp-{node}"
  CELERY_BEAT_SCHEDULE[key] = {
    "task": "sensors.tasks.measure_temp_task",
    "schedule": 5.0, # every 5 second
    "options": {"queue": node}
  }

# create a task queue to differenciate the different nodes created by the distributed system
# command: celery -A iothome worker -Q node-1 -l info
app.conf.task_queues = CELERY_TASK_QUEUES
# runs the command: celery -A iothome beat -l info bt you can run worker and beat: celery -A iothome worker --beat -l info
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE
