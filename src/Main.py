from Task import Task
import os
from colorama import Fore

tasklist = []

def check_list(flags):
    match flags:
        case "-h":
            for task in tasklist:
                print(Fore.BLUE + "`" + task.name + "`", str(task.is_checked()))
        case _:
            i = 0
            for task in tasklist:
                print(Fore.BLUE + str(i), "`" + task.name + "`", str(task.is_checked()))
                i += 1

def line_return():
    inp = input(Fore.WHITE)
    check_command(inp)

def remove_task(flags):
    tasklist.pop(int(flags))

def add_task(flags):
    if flags  == 'a':
        name = input(Fore.GREEN + "Enter the task name: " + Fore.WHITE)
    else: name = flags
    tasklist.append(Task(name))

def switch_task(flags):
    chan = ''
    if isinstance(flags, str) or isinstance(channel, str):
        if flags == 's':
            chan = input(Fore.GREEN + "Please Enter the Index of the task that ou would like to swtich state: " + Fore.WHITE)
        else: print(Fore.RED + "Are you joking with me, this is not a number at all")
    
    elif isinstance(flags, int):
        chan = int(flags)
    else:
        print("Crazy Boy")  

    try:
        channel = int(chan)
        tasklist[channel].set_check(not tasklist[channel].is_checked())  
    except:
        print(Fore.RED + "An Error has benn detected, \n " + Fore.YELLOW + "1) Maybe You didn't type a number, \n 2) Maybe the Index you used don't exists (use the command 'l' to show the tasks and their indexs, \n 3) Or maybe it's just the bad code :)")

def check_command(inputs):
    flags = inputs.split().pop()
    match inputs.split()[0]:
        case 'l':
            check_list(flags)
            line_return()
        case 'a':
            add_task(flags)
            line_return()
        case 'k':
            remove_task(flags)
            line_return()
        case 's':
            switch_task(flags)
            line_return()
        case 'c':
            os.system('clear')
            line_return()
        case 'q':
            print('\n' + Fore.RED + "Goodbye Moonman...")
            exit()
        case _:
            print(Fore.YELLOW + "This command is not valide, please retry ('q' to quit):")
            line_return()
line_return()