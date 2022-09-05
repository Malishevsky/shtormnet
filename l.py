# with open('name.txt','w') as doc_name:
#     doc_name.write('Алексей Янчиц')



g = """
    Введите:
    1 для добавления задачи 
    2 для создания чистого списка 
    3 для вывода стека 
    4 для вывода списка
    5 показать текущий список дел
    6 удалить последнюю задачу
    0 для завершения работы3
    """
class Task():

    def __init__(self):
        pass
    

    def reading(self):
       with open('task.txt','r') as self.task:
            return (self.task.read().split('/'))
            

    def append_task(self):
        inp = ''
        while inp != 'stop':
            inp = input('Добавьте задачу -- >>  ')
            if inp == 'q':
                print(g)
                break
            inp = f'{inp}/'
            with open('task.txt','a') as self.task:
                self.task.write(inp)

    def clear(self):
        with open('task.txt','w') as self.task:
            self.task.write('')
            print('Список дел task.txt очищен')
    def stek(self):
        a = self.reading()
        a.pop(-1)
        print('Стек задач',a)
        for i in reversed(a):
            print(f'Выполнено "{i}"')

    def queue(self):
        a = self.reading()
        a.pop(-1)
        print('Список задач', a)
        for i in a:
            print(f'Выполнено "{i}"')

    def view(self):
        a = self.reading()
        a.pop(-1)
        print(f'Списко дел{a}')

    def del_task(self):
        with open('task.txt','r') as self.task:
            a = self.task.read().split('/')
            a.pop(-1)
            a.pop(-1)
            b = ''
            for i in a:
                b += f'{i}/'
        with open('task.txt','w') as self.task:
                self.task.write(b)
a = Task()


print(g)
while True:

    d = int(input('--->>>>  '))
    
    if d == 1:
        print(g)
        a.append_task()
    elif d == 2:
        print(g)
        a.clear()
    elif d == 3:
        print(g)
        a.stek()
    elif d == 4:
        print(g)
        a.queue()
    elif d == 5:
        a.view()
    elif d == 5:
        a.del_task()
    else:
        a.del_task()

