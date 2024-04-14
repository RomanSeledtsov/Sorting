def Bubble_sort(mass):
    n = len(mass)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
    return mass


def binary_search(find_obj, lst):
    pos = 0
    RusultOk = False
    first = 0
    last = len(lst) - 1
    while first < last:
        middle = (first + last) // 2
        if lst[middle] == find_obj:
            first = middle
            last = first
            RusultOk = True
            pos = middle
        elif find_obj < lst[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if RusultOk:
        print("The element found!, index", pos)
    else:
        print("The element not found.")


from random import randint as gen_nums

my_list = []
for num in range(11):
    my_list.append(gen_nums(0, 101))
print("Unsorted list:", my_list)
sorted_list = Bubble_sort(my_list)
print("Sorted list:", sorted_list)
search = int(input("Your finding object:"))
binary_search(search, sorted_list)
