weight = int(input("Enter weight in kilograms: "))
length = int(input("Enter length in centimeters: "))
width = int(input("Enter width in centimeters: "))
height = int(input("Enter height in centimeters: "))
dimension = length * width * height


if dimension > 100000 and weight > 27:
    print("too large and too heavy")
elif weight > 27:
    print("too heavy")
elif dimension > 100000:
    print("too large")

input()