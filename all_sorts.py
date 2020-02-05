"""
def insertion_sort(list0):
    for i in range(1, len(list0)):
        key = list0[i]
        for j in range(i, -1, -1):
            if j > 0 and key < list0[j-1]:
                list0[j] = list0[j-1]
            else:
                list0[j] = key
                break
    return list0
"""

def insertion_sort(list0):
    for i in range(1, len(list0)):
        key = list0[i]
        for j in range(i):
            if key < list0[j]:
                list0.pop(i)
                list0.insert(j, key)
                break
    return list0


def selection_sort(list0):
    for i in range(len(list0)-1):
        key = list0[i]
        seq = i
        for j in range(i, len(list0)):
            if key > list0[j]:
                key = list0[j]
                seq = j
        temp = list0[i]
        list0[i] = list0[seq]
        list0[seq] = temp
    return list0



if __name__ == '__main__':
    list1 = [5, 7, 4, 3, 1, 2, 6, 0]
    # list1 = [1,2,2,3,4,5,6]
    print(list1)
    list2 = insertion_sort(list1)
    #list2 = selection_sort(list1)
    print(list1)
    print(list2)