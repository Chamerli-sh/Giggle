class Task():
    check = False
    
    def __init__(self, name):
        self.name = name

    def set_check(self):
        Task.check = True

    def uncheck(self):
        Task.check = False
    
    def is_checked(self):
        return Task.check
