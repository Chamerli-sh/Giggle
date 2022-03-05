class Task():
    check = False
    
    def __init__(self, name):
        self.name = name

    def set_check(self, state=False):
        Task.check = state
    
    def is_checked(self):
        return Task.check

    def str_check(self):
        match self.check:
            case True:
                return '✅'
            case False:
                return '❌'