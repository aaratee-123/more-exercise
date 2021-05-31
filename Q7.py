# Ek number ka factorial 1 se leke uss number tak ke saare numbers ko ek saath multiply karke nikalta hai. 
# * Jaise 3 ka factorial 6 hai. Kyunki 1 * 2 * 3 ko calculate karke 6 aata hai
# 4 ka factorial 24 hai. Kyunki 1 * 2 * 3 * 4 ko calculate karke 24 aata hai
# Aise hi 7 ka factorial 5040 hai. Kyunki 1 * 2 * 3 * 4 * 5 * 6 * 7 ko calculate karke 5040 aata hai

i=int(input("enter the number"))
fact=1
while i>0:
    fact=fact*i
    i=i-1
print("factorial",fact)