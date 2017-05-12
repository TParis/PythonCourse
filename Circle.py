from math import pi, pow

def main():
    "Given a radius, will calculate the diameter, circumference, and area of a circle"
    radius = int(input("Please enter the radius of a circle: "))
    print("The diameter is: {0:.2f}".format(radius * 2))
    print("The circumference is: {0:.2f}".format(radius * pi))
    print("The area is: {0:.2f}".format(pow(radius, 2) * pi))


if __name__ == "__main__":
    main()