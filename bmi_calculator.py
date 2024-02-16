print("Welcome to BMI Calculator")

weight_in_kg=int(input("Enter your weight in kg?"))
height_in_m=int(input("Enter you height in meters"))
resultent_bmi=int(weight_in_kg/(pow(height_in_m,2)))

if resultent_bmi<18.5:
    print(f"Your BMI is {resultent_bmi}, you are underweight!")
elif resultent_bmi<25:
    print(f"Your BMI is {resultent_bmi}, you have normal weight!")
elif resultent_bmi<30:
    print(f"Your BMI is {resultent_bmi}, you are slightly overweight!")
else:
    print(f"Your BMI is {resultent_bmi}, you are fucking fat guy!")

