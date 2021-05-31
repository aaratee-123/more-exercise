marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
def max_marks():
    i=0
    while i<1:
        j=0
        while j<=len(marks[i]):
            b=max(marks[j])
            print("max",b)
            j=j+1
        i=i+1
max_marks()