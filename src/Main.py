from Task import Task

tasko = Task("Hello")
print(tasko.name)
tasko.set_check()
print(tasko.is_checked())



tasklist = []

tasklist.append(tasko)
def check_list():
    for task in tasklist:
        print("`" + task.name + "`", str(task.is_checked()))

def line_return():
    inp = input()
    check_command(inp)

def check_command(inputs):
    match inputs.split()[0]:
        case 'l':
            check_list()
            line_return()
        case 'q':
            exit()

line_return()