
def convert_t_to_m(h,m):
    return h*60+m

def convert_m_to_t(m):
    h = m//60
    m = m%60
    return h,m

def add_person_to_list(x,Guard_list):
    if x not in Guard_list:
        Guard_list.append(x)
    return Guard_list


class Guard:
    def __init__(self, name, group, number_of_time_to_get_up):
        self.name = name
        self.group = group
        self.number_of_time_to_get_up = number_of_time_to_get_up
        self.time_already_woke = 0