
CheckGreater = lambda No: (No % 3 == 0) and (No % 5 == 0)

def main():
    print("Enter the size of list ")
    size = int(input())

    print("Enter the numbers :")
    numlist = []
    for i in range(size):
        ndata = int(input())
        numlist.append(ndata)

    Fdata = list(filter(CheckGreater, numlist))
    print("Provided Numbers",numlist)
    print(f"Numbers which are divisible by 3 and 5 :",Fdata)

if __name__ == "__main__":
    main()