# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko 
# yeh sab rule follow karne chaiye:Kam se kam uski length 6 honi chaiye Jada se jada length 16 se 
# jyada na hoKam se kam ek dollar ka sign ($) hona chaiyeKam se kam password mein 2 ya 8 hona chaiye
# Password mein capital A ya capital Z hona chaiye Agar password yeh rules follow kar 
# raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo

ch=input("enter the alphabbate")
if ch>"A" or ch<"Z":#and ch>"a" or ch<"z":
    print(ch)
    special_character=input("enter the special character")
    if special_character=="$": #or sp=="@" or sp=="#":
        print(special_character)
        num=int(input("enter the number"))
        if num>0:
            print(ch+special_character+str(num))
            print("strong password")
        else:
            print("weak password")  
    else:
        print("wrong special character")
else:
    print("wrong alphabate")


