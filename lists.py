def remove_elements(list):
    for i in range (len(list)-1,-1,-1):
        if (i == 0 or i == 4 or i == 5):
            del list[i]
    return list

def add_elements(list):
    list.insert(0, 'Pink')
    list.insert(len(list),'Yellow')
    return list

def is_empty (list):
    return not bool(list)
    
def check_lists(list1, list2):
    if len(list1) > 2 and len(list2)>2:
        return list1[2] == list2[2]
    return False

def list_of_lists(matriz):
    new_list = [matriz[0][0:2], matriz[1][1:4], matriz[2][-2:]]
    return new_list
