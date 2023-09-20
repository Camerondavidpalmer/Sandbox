length = int(input("Length: "))
password = input("Enter a password:")
while len(password) < length:
    print("Invalid length")
    password = input("Enter a password:")
number_of_asterisks = len(password)
print("*" * number_of_asterisks)
