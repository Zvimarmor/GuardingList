from datetime import datetime
from additionalfunc import *

def easy_case(total_time, Guard_list):
    total_time = convert_t_to_m(total_time)
    
    if Guard_list.number_of_guards == 0:
        return "error: no guard in the list"
    
    if Guard_list.number_of_guards == 1:
        for name in range:
            return Guard_list.list[name]
        
    if total_time == 0:
        return "No one is getting up"

    time_for_each = total_time//Guard_list.number_of_guards
    for name in range(Guard_list.number_of_guards):
        currentguard = Guard_list.list[name]
        currentguard.guard_time = time_for_each
    return Guard_list

def hard_case(total_time, Guard_list):
    total_time = convert_t_to_m(total_time[0], total_time[1])
    
    if Guard_list.number_of_guards == 0:
        return "error: no guard in the list"
    
    if Guard_list.number_of_guards == 1:
        for name in range(Guard_list.number_of_guards):
            return Guard_list.list[name]
        
    if total_time == 0:
        return "No one is getting up"
    
    time_for_each = total_time//Guard_list.number_of_guards
    for name in range:
        currentguard = Guard_list.list[name]
        currentguard.guard_time = time_for_each
    return Guard_list

def main(total_time, Guard_list, current_time):
    total_time = convert_t_to_m(total_time)

    if is_time_devide_beautifully(total_time):
        easy_case(total_time, Guard_list)
    else:
        hard_case(total_time, Guard_list)
    
    for name in range(Guard_list.number_of_guards):
        currentguard = Guard_list.list[name]
        if currentguard.guard_time == 0:
            print(name, "is guarding now for", convert_m_to_t(Guard_list.list[name].guard_time), "minutes")
            currentguard.guard_time -= 1
            currentguard.time_already_woke += 1
            break

    print("Time to guard is over")
    return

    
if __name__ == "__main__":
    Guard_list = Guard_list()
    Guard_list.add_guard(Guard("John", "Group1", 0))
    Guard_list.add_guard(Guard("Doe", "Group1", 0))
    Guard_list.add_guard(Guard("Jane", "Group2", 0))
    Guard_list.add_guard(Guard("Smith", "Group2", 0))
    Guard_list.add_guard(Guard("Jack", "Group3", 0))
    Guard_list.add_guard(Guard("Jill", "Group3", 0))
    current_time = datetime.now()

    main(1.5, Guard_list, current_time)


