from source import create
from helpers import find_task

tmp_str = ''
while tmp_str != 'exit':
    tmp_str = input('choose your function:'
                    'create,'
                    ' find,'
                    ' mark task,'
                    ' change priority,'
                    ' delete'
                    ' tasks by adding'
                    ' tasks by priority'
                    ' not implemented'
                    ' overdue'
                    ' statistic'
                    ' save list'
                    ' download data'
                    ' exit'
                    ' \n')
    if tmp_str == 'create':
        create.create_entry()
        create.write_data()
        create.screen_clear()
    elif tmp_str == 'find':
        find_task.search_title()
        create.screen_clear()
    elif tmp_str == 'mark task':
        create.mark_task()
        create.screen_clear()
    elif tmp_str == 'change priority':
        create.change_priority()
        create.screen_clear()
    elif tmp_str == 'delete':
        create.delete_task()
        create.screen_clear()
    elif tmp_str == 'tasks by adding':
        create.adding_task()
        create.screen_clear()
    elif tmp_str == 'tasks by priority':
        create.task_priority()
        create.screen_clear()
    elif tmp_str == 'not implemented':
        create.unimplemented()
        create.screen_clear()
    elif tmp_str == 'implemented':
        create.implemented()
        create.screen_clear()
    elif tmp_str == 'overdue':
        create.overdue()
        create.screen_clear()
    elif tmp_str == 'statistic':
        create.statistic()
        create.screen_clear()
    elif tmp_str == 'save list':
        create.save_csv()
        create.screen_clear()
    elif tmp_str == 'download data':
        create.read_data()
        create.screen_clear()
    else:
        create.write_data()
        break


