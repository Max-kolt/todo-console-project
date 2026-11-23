from tasks import add_task, view_tasks, delete_task, \
    complete_task, view_completed_tasks, save_to_file


def user_input(text: str, valid_input: list = None ):
    while True:
        a = input(text)
        if a.lower().strip() in valid_input:
            return a
        else:
            print('Неверный ввод. Вы можете указать один из этих значений:', 
                ", ".join(valid_input) )

try:
    while True:
        a = user_input(
            text = "\n\n\nЗдравствуйте! Введите пункт меню: \n" +
                    "1. Добавить задачу \n" +
                    "2. Просмотреть задачи \n" +
                    "3. Удалить задачу \n" +
                    "4. Выполнить задачу \n" +
                    "5. Список выполненных задач \n" +
                    "0. Выйти \n\n" +
                    "Ваш выбор: ",
            valid_input=["1", "2", "3", "4", "5", "0"]
        )

        # a = int(input(
        #     "\n\n\nЗдравствуйте! Введите пункт меню: \n" \
        #     "1. Добавить задачу \n" \
        #     "2. Просмотреть задачи \n" \
        #     "3. Удалить задачу \n" \
        #     "0. Выйти \n\n" \
        #     "Ваш выбор: " 
        # ))

        match a:
            case "1": 
                new_task = input(
                    f"{'-'*5} Добавыить задачу {'-'*5}\n" \
                    "Название задачи: "
                )
                add_task(new_task)
            case "2":
                print(f"{'-'*5} Список задач {'-'*5}")
                view_tasks()
            case "3":
                id_task = int(input(
                    f"{'-'*5} Удаление задачи {'-'*5}\n" \
                    "Номер задачи: "
                ))-1
                delete_task(id_task)
            case "4":
                id_task = int(input(
                    f"{'-'*5} Выполнение задачи {'-'*5}\n" \
                    "Номер задачи: "
                ))-1
                complete_task(id_task)
            case "5":
                print(f"{'-'*5} Список задач {'-'*5}")
                view_completed_tasks()
            case "0": 
                save_to_file()
                print('BYE')
                break
            # case _:
            #     print("Вы ввели неверный пункт")

        input('Продолжить...')

except KeyboardInterrupt:
    save_to_file()
    print("Вы нажали ctrl+c, программа принудительно закрывается. \n" \
    "Все данные сохраненны.")
except Exception as e:
    print(e) 
    
    
