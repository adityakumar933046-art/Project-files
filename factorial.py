numb = int(input("Enter a number: "))
factorial = 1

for i in range(1, numb + 1):
    factorial *= i

print("Factorial of", numb, "is:",factorial)