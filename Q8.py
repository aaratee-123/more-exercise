string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
# i=0
# t=[]
# while i<len(string_list):
#     j=i+1
#     while j<len(string_list):
#         if string_list[i]==string_list[j]:
#             t.append(string_list[i])
#         j=j+1
#     i=i+1
# print(t)

i=0
a=[]
while i<len(string_list):
    b=string_list[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)
