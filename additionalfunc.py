
def convert_t_to_m(h,m):
    return h*60+m

def convert_m_to_t(m):
    h = m//60
    m = m%60
    return h,m

def is_time_devide_beautifully(h,m):
    new_time = convert_t_to_m(h,m)
    if new_time%30 == 0:
        return True
    return False

class Guard:
    def __init__(self, name, group, number_of_time_to_get_up):
        self.name = name
        self.group = group
        self.number_of_time_to_get_up = number_of_time_to_get_up
        self.time_already_woke = 0

class Guard_list:
    def __init__(self):
        self.list = {}

    def add_guard(self, guard):
        self.list[guard.name] = guard.name
        self.list[guard.group] = guard.group
        self.list[guard.number_of_time_to_get_up] = guard.number_of_time_to_get_up
        self.list[guard.time_already_woke] = guard.time_already_woke

    def print_list(self):
        for name in self.list:
            print(name, self.number_of_time_to_get_up)





