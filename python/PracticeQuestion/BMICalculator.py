#Create a BMI calculator. 
ch = int(input("choose 1 for height in cm and 2 for heighr in metre: ", ))
if ch == 1:
    weight = int(input("Enter your weight: "))
    height = int(input("enter your height in cm: "))
    BMI = weight * 1000 / (height**2)
    print ("Your body mass index is : ", BMI)

elif ch == 2:
    weight = int(input("Enter your weight: "))
    height = int(input("enter your height in metre: "))
    BMI = weight / (height**2)
    print ("Your body mass index is : ", BMI)

else:
    print(" invalid choice")