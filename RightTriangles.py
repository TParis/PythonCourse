from math import sqrt, pow

def main():
    "Calculates all possible integer values for a, b, c of the pythagorean thereom where a and b are whole numbers between 1 and 20"
    counter = 0
    for i in range(1, 21):
        for j in range(1, 21):
            c = sqrt(pow(i, 2) + pow(j, 2))
            counter += 1
            print("{}) a: {:.2f}, b: {:.2f}, c: {:.2f}".format(counter, i, j, c))

if __name__ == "__main__":
    main()