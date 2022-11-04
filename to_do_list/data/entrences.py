import datetime
import json

list_of_task = []
TEST_DATA = [
    {
        "id": 1,
        "title": "Shopping",
        "description": "Grocery shopping",
        "priority": 4,
        "due_date": datetime.datetime(2022, 11, 1, 12, 37),
        "done": False
    },
    {
        "id": 2,
        "title": "Sleeping",
        "description": "Go to sleep",
        "priority": 2,
        "due_date": datetime.datetime(2022, 11, 2, 22, 10),
        "done": True
    },
    {
        "id": 3,
        "title": "Working",
        "description": "Go to work",
        "priority": 1,
        "due_date": datetime.datetime(2022, 7, 3, 7, 20),
        "done": False
    },
    {
        "id": 4,
        "title": "Dinner",
        "description": "Cooking a dinner",
        "priority": 3,
        "due_date": datetime.datetime(2022, 8, 4, 8, 00),
        "done": False
    }

]


