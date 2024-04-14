
def convert_t_to_m(t):
    return t*60

def convert_m_to_t(t):
    h = t//60
    m = t%60
    return h+(m/100)

def is_time_devide_beautifully(time):
    new_time = convert_t_to_m(time)
    if new_time%30 == 0:
        return True
    return False

class Guard:
    def __init__(self, name, group, guard_time):
        self.name = name
        self.group = group
        self.guard_time = guard_time
        self.time_already_woke = 0

class Guard_list:
    def __init__(self):
        self.list = {}
        self.number_of_guards = 0

    def add_guard(self, guard):
        self.list[guard.name] = guard.name
        self.list[guard.group] = guard.group
        self.list[guard.guard_time] = guard.guard_time
        self.list[guard.time_already_woke] = guard.time_already_woke
        self.number_of_guards += 1

    def print_list(self):
        for name in self.list:
            print(name, self.guard_time)





