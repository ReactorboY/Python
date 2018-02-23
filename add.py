#  binary search
a = [2,5,6,78,25,45,71,96,87,95]

first = 0
last = len(a) - 1
flag = 0
item = int(input("enter number to found "))

while first <= last and not flag:
    mid = (first + last )// 2
    if(a[mid] == item):
        flag = 1
    else:
        if item < a[mid]:
            last = mid - 1
        else:
            first = mid + 1

if flag == 1:
    print("item founded")
else:
    print("item not founded")
