#  Counting of element of matrix
a = [[1,7,5],
     [9,7,2],
     [3,9,5]]

b = []

for i in range(0, len(a)):
    b = b + a[i]

print(b)

# print(el)
leng = len(b)
no = 0
while leng > 0:
    count = 0
    el = b[no]
    for i in range(0,len(b)):
        if (el == b[i]):
            count += 1
    print(count)
    leng -= 1
    no += 1
