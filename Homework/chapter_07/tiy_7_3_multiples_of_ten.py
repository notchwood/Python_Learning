number = int(input("\n Please enter a number: "))
result = number %8
if result == 0:
    print(f"your number {number} is divisable by 8")
else:
    print(f"Your number {number} is not divisable by 8")
print(f"there was a remainder of {result} ")