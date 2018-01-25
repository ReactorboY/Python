a = [[1,2], [2,3]]

def countMe(list, elm):
    count = 0
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if (list[i][j] == elm):
                count += 1
    print(count)

countMe(a,1)
