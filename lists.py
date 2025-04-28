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

def check_list(list1, list2):
    if len(list1) > 2 and len(list2)>2:
        return list1[2] == list2[2]
    return False

#No sabia que no tiraba error list[0:2] cuando len(list) < 2, mal ahi compa
def list_of_lists(matriz):
    new_list = []
    cont_list = 1
    for list in matriz:
        if(cont_list == 1):
            if len(list) > 1:
                new_list.append(list[0:2])
            else:
                new_list.append(list[0:1])
        if(cont_list == 2):
            if len(list) >= 4:
                new_list.append(list[1:4])
            elif len(list) == 3:
                new_list.append(list[1:3])
            elif len(list) == 2:
                new_list.append(list[2])
        if(cont_list == 3):
            if len(list) > 1:
                new_list.append(list[-2:])
            else: 
                new_list.append(list[-1:])
        cont_list = cont_list + 1
    return new_list
