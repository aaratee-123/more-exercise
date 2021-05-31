#  program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul ka ek 
# mahine ka kharcha nikalenge input ka use kar ke do values ka input lo: * Number of students
# Ek student ka kharcha
# Iss
# Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya usse kam hai toh print 
# karein "Hum budget ke andar hain" nahi toh print karo ki hum budget ke bahar hain. Note: Inn exercises 
# mein aapko variables ke naam apne aap soch kar likhne hain
num=int(input("enter the number of students"))
counter=0
Ek_student_ka_Kharcha=250
t=Ek_student_ka_Kharcha
sum=0
i=1
while i<=num:
    counter=counter+1
    sum=sum+t
    i=i+1
print("sum=",sum,":counter=",counter)
if sum<50000:
    print("Hum budget ke andar hain")
else:
    print("Hum budget ke andar nahi hain")