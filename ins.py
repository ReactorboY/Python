a = [4,6,1,3,88,12]

for i in range(1, len(a) ):
    min = a[i]
    i = i - 1
    while i >= 0:
        if min < a[i]:
            a[i+1] = a[i]
            a[i] = min
            i = i - 1
        else:
            break

print(a)
