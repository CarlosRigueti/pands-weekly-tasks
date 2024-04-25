# Program that print square root of a positive number.
# Autor : Carlos Rigueti

x = float(input("Please enter a positive number: "))
a = x
while abs(x - (a * a)) > 0.00001:
    p = (a + (x / a)) / 2
    a = p
print(f"The square root of {x} is approx {p:.5f}.")