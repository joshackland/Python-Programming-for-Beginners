age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age < 18 or country == "USA" and age < 21:
    print("You are too young to enter")
else:
    print("You are allowed to enter")