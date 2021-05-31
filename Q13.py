a = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
i = 0
while i < len(a):
    small_list_length = len(a[i])
    j = 0
    while j < small_list_length:
        print (a[i][j])
        j=j + 1
    i=i + 1
