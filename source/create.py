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


class Task:

    def __init__(self, id: int, title: str, description:str, priority: int, due_date: datetime, done: bool) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date,
        self.done = done
        list_of_task.append(self)

    def my_time(self):
        year = int(input('please enter year: \n'))
        month = int(input('please enter month: \n'))
        day = int(input('please enter day: \n'))
        hour = int(input('please enter time: \n'))
        minutes = int(input('please enter minutes: \n'))
        good_time = datetime.datetime(year, month, day, hour, minutes)
        return good_time

    def create(self):
        self.id = 1
        self.title = input('Please create a task`s name: \n')
        self.description = input('Please describe your task: \n')
        self.priority = int(input('Please put task priority from 1 to 10: \n'))
        self.due_date = self.my_time()
        self.done = bool(input('If you completed, type anything<3'))


    def mark_task(self):
        '''Do mark as done task'''
        if self.done in find_task.search_title() == 'False':
            self.done = 'True'


    def change_priority(self):
        '''Changing priority of particular task'''
        new_priority = input('Please enter a new priority for task:\n')
        print(f'You are going to reset priority from {self.priority} to {new_priority}')
        agree = input('Do you really want to reset? y/n \n')
        if agree == 'y':
            self.priority = new_priority


    def delete_task(self):
        '''Delete a particular task from list of tasks'''
        find_task.search_title()
        for task in find_task.search_title():
            if task in find_task.search_title():
                return list_of_task.remove(task)


    def adding_task(self):
        '''Print all planned task names by their adding'''
        for list in list_of_task:
            for self.done in list:
                if self.done is not True:
                    for self.id in list_of_task:
                        if self.id <= 1:
                            print(self.title)
                            self.title += 1


    def task_priority(self):
        '''Print all planned task names in descending order of priority'''
        for list in list_of_task:
            for self.done in list:
                if self.done is not True:
                    if self.priority <= len(list_of_task):
                        print(self.title)
                    self.priority += 1

    unimp_task = list()

    def unimplemented(self):
        '''Print all not implemented task names'''
        for list in list_of_task:
            for self.done in list:
                if self.done is not True:
                    print(self.title)
                    self.unimp_task.append(self.title)

    imp_task = list()

    def implemented(self):
        '''Print all implemented task names'''
        for list in list_of_task:
            for self.done in list:
                if self.done is not False:
                    print(self.title)
                    self.imp_task.append(self.title)

    overd_task = list()

    def overdue(self):
        '''Print overdue task name'''
        data_today = datetime.datetime.today()
        for list in list_of_task:
            for self.due_date in list:
                if str(self.due_date) > str(data_today):
                    print(self.title)
                    self.overd_task.append(self.title)


    def statistic(self):
        num_task = list_of_task.count()
        print(f'Your total number of task: {num_task}')
        print(f'Your total number of implemented task: {self.imp_task.count(all(self.imp_task))}')
        print(f'Your total number of not implemented task: {self.unimp_task.count(all(self.unimp_task))}')
        print(f'Your total number of overdue task: {self.overd_task.count(all(self.overd_task))}')


def save_csv():
    '''Saving input data in particular file'''
    with open('test_data.csv', 'w', newline='') as csvfile:
        csvlist = csv.writer(csvfile)
        csvlist.writerow(list_of_task)


def read_data():
    '''json read'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'r') as test_data_info:
        load_data = json.load(test_data_info)
        return load_data


def write_data():
    '''json write'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'w') as test_data_info:
        json.dump(list_of_task, test_data_info)


def write_testdata():
    '''Write testing data in file'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', "tasks.json")
    with open(file_path, 'w') as test_data_info:
        json.dump(TEST_DATA, test_data_info)












