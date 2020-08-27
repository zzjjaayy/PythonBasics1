userWeight = input("Enter your Weight: ")
userWeightInt = int(userWeight)

userMeasure = input("(L)bs or (K)gs: ").upper()

if userMeasure == "L":
    print(f"{userWeightInt/2.2} Kgs")
elif userMeasure == "K":
    print(f"{userWeightInt*2.2} Lbs")
else:
    "Error"
