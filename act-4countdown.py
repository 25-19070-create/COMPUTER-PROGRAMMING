n = int(input("Enter n: "))
while n < 1:
    print("Invalid! Enter a positive number.")
    n = int(input("Enter n: "))
while n > 0:
    print(n, end=" ")
    n -= 1
print("Liftoff!")
