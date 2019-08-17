print('Hello world!')
age = 17
#Teste sur les conditions
if age >= 18 :
    print("Vous êtes majeur, merci.")
else:
    print("Vous êtes mineur, merci.")
age = 7
#Teste de plusieurs conditions en un même temps,interval
if(age > 10 and age <= 16):
    print(" et en même temps adolescent :).")
elif (age > 16 and age <= 35):
    print("et en même temps jeunes :).")
else:
    print("et en même temps vieux :).")
def bonjour (name):
    print("Bonjour "+ name)
bonjour("Za")
