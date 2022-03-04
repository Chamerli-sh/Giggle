from Task import Task

tasklist = []

def check_list(flags):
    match flags:
        case "-h":
            for task in tasklist:
                print("`" + task.name + "`", str(task.is_checked()))
        case _:
            i = 0
            for task in tasklist:
                print(i, "`" + task.name + "`", str(task.is_checked()))
                i += 1

def line_return():
    inp = input()
    check_command(inp)

def remove_task(flags):
    tasklist.pop(int(flags))

def add_task():
    name = input("Enter the task name: ")
    tasklist.append(Task(name))

def switch_task(flags):
    if isinstance(flags, str):
        if flags == 's':
            channel = int(input("Please Enter the Index of the task that ou would like to swtich state: "))
        else: print("Are you joking with me, this is not a number at all")
    
    elif isinstance(flags, int):
        channel = int(flags)
    else:
        print("Crazy Boy")
    
    tasklist[channel].set_check(not tasklist[channel].is_checked())

def check_command(inputs):
    flags = inputs.split().pop()
    match inputs.split()[0]:
        case 'l':
            check_list(flags)
            line_return()
        case 'a':
            add_task()
            line_return()
        case 'k':
            remove_task(flags)
            line_return()
        case 's':
            switch_task(flags)
            line_return()
        case 'q':
            exit()
        case _:
            print("This command is not valide, please retry ('q' to quit):")
            line_return()
line_return()