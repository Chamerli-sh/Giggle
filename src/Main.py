from Task import Task

tasko = Task("Hello")
print(tasko.name)
tasko.set_check()
print(tasko.is_checked())

tasklist = []

tasklist.append(tasko)

for task in tasklist:
    print("`" + task.name + "`")
