a = [[3,6,1],
     [8,5,4],
     [9,2,7]]

b = []

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if(a[i][j] % 7 == 0):
            a[i][j] = 'Hello'

print(a)
