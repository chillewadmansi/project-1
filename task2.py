num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

print("Basic python skills developed")




