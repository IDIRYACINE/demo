def compare_lists(list1, list2):
    intersection = set(list1) & set(list2)
    only_list1 = set(list1) - set(list2)
    only_list2 = set(list2) - set(list1)
    return (intersection, only_list1, only_list2)
