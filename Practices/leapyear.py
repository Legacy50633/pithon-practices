print("Leaper Checker ?")
year_to_check = int(input("Enter the Year to get checked !: "))
if year_to_check%4 == 0:
    print(f"The year {year_to_check} is a Leap Year")
else:
    print(f"The year {year_to_check} is not a Leap Year")