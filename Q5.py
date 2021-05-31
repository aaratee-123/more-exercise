# input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se 
# sabse bade number ko print karo Note: Isme aap loops ka use nahi kar sakte.

number1=int(input("enter the number"))
number2=int(input("enter the number"))
number3=int(input("enter the number"))
if number1>number2 and number1>number3:
    print("greater number",number1)
elif number2>number1 and number2>number3:
    print("greater number",number2)
else:
    print("greater number",number3)