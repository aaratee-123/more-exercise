list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
output=[1,5,10,12,16]
new_list=[]
i=0
while i<len(list1):
    a=list1[i]
    if a not in list2:
        new_list.append(a)    
    i=i+1
    j=0
while j<len(list2):
    b=list2[j]
    new_list.append(b)
    j=j+1
print(new_list)
