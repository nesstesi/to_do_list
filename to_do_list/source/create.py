import datetime
import json
from data.entrences import list_of_task
from data.entrences import TEST_DATA
from helpers import find_task
import os
from time import sleep
import csv


def screen_clear():
    '''Clear the screen'''
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    sleep(2)


def my_time():
    year = int(input('please enter year: \n'))
    month = int(input('please enter month: \n'))
    day = int(input('please enter day: \n'))
    hour = int(input('please enter time: \n'))
    minutes = int(input('please enter minutes: \n'))
    good_time = datetime.datetime(year, month, day, hour, minutes)
    return good_time


def create_entry():
    '''Create new entry in To Do list'''
    entry = dict({'id': 1,
                  'title': input('Please create a task`s name: \n'),
                  'description': input('Please describe your task: \n'),
                  'priority': int(input('Please put task priority from 1 to 10: \n')),
                  'due_date': my_time(),
                  'Done': bool(input('If you completed, type anything<3'))})
    list_of_task.append(entry)


def mark_task():
    '''Do mark as done task'''
    if 'done' in find_task.search_title() == 'False':
        find_task.search_title()['done'] = 'True'


def change_priority():
    '''Changing priority of particular task'''
    find_task.search_title()
    new_priority = input('Please enter a new priority for task:\n')
    if find_task.search_title()['priority'] != new_priority:
        find_task.search_title()['priority'] = new_priority


def delete_task():
    '''Delete a particular task from list of tasks'''
    find_task.search_title()
    for task in find_task.search_title():
        if task in find_task.search_title():
            return list_of_task.remove(task)


def adding_task():
    '''Print all planned task names by their adding'''
    for tasks in list_of_task:
        for element in list_of_task['done']:
            if element is not True:
                for char in list_of_task['id']:
                    if char <= 1:
                        print(char,['name'])
                    char += 1


def task_priority():
    '''Print all planned task names in descending order of priority'''
    for task in list_of_task:
        for boolean in ['done']:
            if boolean is not True:
                for value in ['priority']:
                    if value <= max(value):
                        print(value,['name'])
                    value += 1

unimp_task = []
def unimplemented():
    '''Print all not implemented task names'''
    for tassk in list_of_task:
        for elemnt in ['done']:
            if elemnt is not True:
                print(['name'])
                unimp_task.append(['name'])


imp_task = []
def implemented():
    '''Print all implemented task names'''
    for task in list_of_task:
        for value in ['done']:
            if value is not False:
                print(['name'])
            imp_task.append(['name'])

overd_task = []
def overdue():
    '''Print overdue task name'''
    data_today = datetime.datetime.today()
    for task in list_of_task:
        for date in ['due_data']:
            if date < str(data_today):
                print(['name'])
            overd_task.append(['name'])


def statistic():
    num_task = list_of_task.count()
    print(f'Your total number of task: {num_task}')
    print(f'Your total number of implemented task: {imp_task.count(all(imp_task))}')
    print(f'Your total number of not implemented task: {unimp_task.count(all(unimp_task))}')
    print(f'Your total number of overdue task: {overd_task.count(all(overd_task))}')


def save_csv():
   '''Saving input data in particular file'''
    with open('test_data.csv', 'w', newline='') as csvfile:
        csvlist = csv.writer(csvfile, list_of_task)

def read_data():
    '''json read'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'r') as test_data_info:
        load_data = json.load(test_data_info)


def write_data():
    '''json write'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'w') as test_data_info:
        json.dump(list_of_task, test_data_info)














