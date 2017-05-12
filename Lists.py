from random import randint

def main():
    "Generates 30 integers and, if they do not already exist in the list, adds them to mylist"
    mylist = []
    for i in range(1, 31):
        rand = randint(1,100)
        if rand not in mylist:
            mylist.append(rand)
        else:
            print("{} is already in list".format(rand))
    print(mylist)

if __name__ == "__main__":
    main()