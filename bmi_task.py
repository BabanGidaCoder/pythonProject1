# calculates a persons BMI
weight = float(input(" Enter your weight in kg:"))
height = float(input(" Enter your height in Meters:"))

bmi = weight / (height * height)  # formula for BMI

if bmi >= 30:
    print(" you are obese!\n")

elif bmi >= 25:
    print("you are overweight!\n")
elif bmi >= 18.5:
    print(" you are normal\n")

else:
    bmi < 18.5
    print("you are underweight!\n")






