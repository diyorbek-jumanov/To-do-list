def Add(create_task, state, text):
    '''
    creating new task
    Parametrs:
        create_task(dict): Given a dictionary
        state(bool): Given a boolen
        text(str): Given a string
    Returns:
        dict: Returning value
    '''
    create_task['task-name'] = text
    create_task['task-state'] = state
    return create_task


def Remove(todo, idx):
    '''
    Removing task
    Parametrs:
        todo(list) = Given a list
        idx(int) = Given a integer
    Returning:
        list: Returning value
    '''
    del todo[idx]
    return todo

def Update(todo, idx):
    '''
    Update task
    Parametrs:
        todo(list): Given a list
        idx(int) = Given a integer
    Returning:
        list: Returning value
    '''
    title = input('qanday nomga o\'zgartirmoqchisiz? ')
    state = input('taskni holatini kiriting bajarilgan bolsa True aks holda False --> ')
    if state.lower() == 'true':
        state = True
    else:
        state = False
    todo[idx].update({"task-name": title, "task-state": state})
    return todo
    
def Checking(todo, idx):
    '''
    Checking list
    Parametrs:
        todo(list): Given a list
        idx(int) = Given a integer
    Returning:
        list: Returning value
    '''
    if todo[idx]['task-state'] == True:
        print('task bajarilgan')
    else:
        print('task bajarilmagan')

def Create_list(todo):
    '''
    Creating new list
    Parametrs:
        todo(list): Given a list
    Returning:
        list: Returning value
    '''
    add_q = input('task qo\'shasizmi? ')
    if add_q.lower() == 'ha':
        empty_dict = dict()
        task_name = input('task nomini kiriting --> ')
        task_state = input('task holatini kiriting bajarilgan bolsa True aks holda False --> ')
        if task_state.lower() == 'true':
            task_state = True
        else:
            task_state = False
        todo.append(Add(empty_dict, task_state, task_name))
    
    remove_q = input('taskni o\'chirishni hohlaysizmi? ')
    if remove_q.lower() == 'ha':
        idx = int(input('qaysi indexdagi taskni? '))
        todo = Remove(todo, idx)

    update_q = input('taskni update qilishni hohlaysizmi? ')
    if update_q.lower() == 'ha':
        idx = int(input('qaysi indexdagi taski update qimoqchisiz? '))
        todo = Update(todo, idx)

    checking_q = input('taskni checking qilishni hohlaysizmi? ')
    if checking_q == 'ha':
        idx = int(input('qaysi indexdagi taskni checking qimoqchisiz? '))
        Checking(todo, idx)

    print(todo)

def Clear(todo):
    '''
    Clearing list
    Parametrs:
        todo(list): Given a list
    Returning:
        list: Returning value
    '''
    return todo.clear()

def Count(todo):
    '''
    Counting task
    Parametrs:
        todo(list): Given a list
    Returning:
        int: Returning value
    '''
    return len(todo)

def get_task_true(todo):
    count = 0
    for i in len(todo):
        if i['task-state'] == True:
            count += 1
    return count

def get_task_false(todo):
    count = 0
    for i in len(todo):
        if i['task-state'] == False:
            count += 1
    return count


lst = list()
Create_list(lst)
