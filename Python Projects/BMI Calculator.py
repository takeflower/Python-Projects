height = float(input("Enter your height in cm: "))

weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print(BMI)

if BMI <= 18.4:
    print("You are underweight. Add for your diet more callories")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight. Start to eat less unhelathy food, do sports")
elif BMI <= 34.9:
    print("You are severely over weight. You should change your diet immediately")
elif BMI <= 39.9:
    print("You are obese. Walk everyday, never look at unhelathy food, drink more water")
else:
    print("You are severely obese. Extreme diet or help of doctors")

input()