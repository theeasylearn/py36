# 1 2 3 4 5  
# 1 2 3 4  
# 1 2 3  
# 1 2  
# 1
temp = 5;
for i in range(1,6):
    for j in range(1, temp + 1):
        print(j, end=' ')
    print('')
    temp = temp -1