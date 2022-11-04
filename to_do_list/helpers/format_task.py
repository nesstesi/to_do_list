
def human_print(entry):
    '''Print entry of todo list in normal view'''
    for key in entry:
        if key != 'due_date':
            print(key, entry[key])
        else:
            print(key, entry[key].strftime('%d/%m/%Y %H:%M'))