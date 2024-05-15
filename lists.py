def remove_elements(list_to_remove_elements):
    del list_to_remove_elements[4:6]
    del list_to_remove_elements[0:1]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    
    list_to_add_elements = ["Pink"]+list_to_add_elements+["Yellow"]
    if len(list_to_add_elements) == 0:
        return "Nothing"  # Remove this line and implement
    if len(list_to_add_elements)>0:
        return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False 



def check_lists(list_to_compare1, list_to_compare2):
    list1and2 = list_to_compare1[2:3] == list_to_compare2[2:3]
    return list1and2  # Remove this line and implement


def list_of_lists(list_of_lists_to_modify):
    
   return [list_of_lists_to_modify[0][0:2]]+[list_of_lists_to_modify[1][1:4]]+[list_of_lists_to_modify[2][-2:]]
#Sample List: [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
#Sample Output: [[1, 2], [5, 6, 7], [11, 12]
# Remove this line and implement
