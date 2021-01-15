def Add(create_task, state, text):
    create_task['task-name'] = text
    create_task['task-state'] = state
    return create_task

def Remove(todo, idx):
    del todo[idx]
    return todo

# def Update(todo, ):


# def Checking(state):


def Create_list(todo):
    create_task = dict()
    text = 'javascript'
    todo.append(Add(create_task, False, text))
    idx = 0
    todo = Remove(todo, idx)
    print(todo)
    # Update()
    # Checking(state)
# def Clear(todo)
# def Count(state)
todo = list()
Create_list(todo)