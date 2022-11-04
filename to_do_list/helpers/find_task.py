from data.entrences import list_of_task
from helpers import format_task


def search_title():
    '''Searching the task by the name of title'''
    part_of_name = input('Please enter a part of title`s name:\n')
    for entry in list_of_task:
        for part_of_name in entry:
            if part_of_name in entry:
                return format_task.human_print(entry)