a = [[5,1], [2,1],[9,6]]
b = []
# c = [[0,0], [0,0]]
# count = 0

# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         b[count] = a[i][j]
#         count += 1

for i in range(0,len(a)) :
    b=b+a[i]
print (b)

for i in range(0, len(a)):
    for j in range(0, len(b) - 1):
        if (b[j] > b[j+1]):
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp

print(b)
# print [5,1,2,1]
