def Add(create_task, state, text):
    create_task['task-name'] = text
    create_task['task-state'] = state
    return create_task

def Remove(todo, idx):
    del todo[idx]
    return todo

def Update(todo, idx):
    title = input('qanday nomga o\'zgartirmoqchisiz? ')
    state = input('taskni holatini kiriting bajarilgan bolsa True aks holda False --> ')
    if state.lower() == 'true':
        state = True
    else:
        state = False
    todo[idx].update({"task-name": title, "task-state": state})
    return todo
    
def Checking(todo, idx):
    if todo[idx]['task-state'] == True:
        print('task bajarilgan')
    else:
        print('task bajarilmagan')

def Create_list(todo):
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
lst = list()
Create_list(lst)
