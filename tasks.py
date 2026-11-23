import json


with open("data_tasks.json", "r") as file:
    data_tasks = json.load(file)

tasks = data_tasks["tasks"]
completed_tasks = data_tasks["completed_tasks"]


def save_to_file():
    saving_tasks = {
        "tasks": tasks,
        "completed_tasks": completed_tasks
    }

    with open("data_tasks.json", "w") as file:
        file.write(json.dumps(saving_tasks))
    

def add_task(task: str):
    tasks.append(task)
    print(f"Задача '{task}' добавлена 👍")

def view_tasks():
    if not tasks:
        print("Список пустой, сначала добавьте задачу")
    else:
        # print("Список задач:")
        for ind, task in enumerate(tasks):
            print(f"{ind+1}. {task}")

def delete_task(ind_t: int):
    if tasks and 0 <= ind_t < len(tasks):
        tasks.pop(ind_t)
        print("Задача удалена")
    else:
        print("Ошибка")

def complete_task(ind_t: int):
    if tasks and 0 <= ind_t < len(tasks):
        new_completed_task = tasks.pop(ind_t)
        completed_tasks.append(new_completed_task)
        print(f"Задача '{new_completed_task}' перенесена в список выполненных")
    else:
        print("Ошибка")

def view_completed_tasks():
    if not completed_tasks:
        print("Список пустой, сначала выполните задачу")
    else:
        # print("Список  задач:")
        for ind, task in enumerate(completed_tasks):
            print(f"{ind+1}. {task}")

