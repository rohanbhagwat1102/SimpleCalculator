#python simple calculator



print("\n\n******Simple Calculator******")

print("\nSELECT OPERATION")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")


choice = int(input("\nEnter choice number: "))

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))


if choice == 1:
    print("\nAdditon: ", num1 + num2)
elif choice == 2:
    print("\nSubtraction: ", num1 - num2)
elif choice == 3:
    print("\nMultiply: ", num1 * num2)
elif choice == 4:
    print("\nDivision: ", num1/num2)
else:
    print("Invalid choice")