weightInKG = int(input("Enter weight in KG: "))
heightInMeters = int(input("Enter height in Meters: "))

bmi : int = weightInKG / (heightInMeters * heightInMeters)

print(f"Your BMI is: {bmi}")
