def check_same_frequency(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)

    if len(list1) != len(list2):
        return False

    if list1 == list2 :
        return True
    else:
        return False


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1,list2))