from random import randint

def main():
    "Generates two random numbers and asks the user to sum them"
    a = randint(0,10)
    b = randint(0,10)
    while True:
        try:
            c = int(input("What is the sum of {} and {}? ".format(a, b)))
            if ((a + b) == c):
                print("Correct!")
                break
            else:
                print("Incorrect!")
        except ValueError:
            print("Invalid Input!")
        print()


if __name__ == "__main__":
    main()