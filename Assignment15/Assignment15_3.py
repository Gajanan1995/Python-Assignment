OddNumbers = lambda No: (No % 2 != 0)

def main():
    listn = []
    print("Enter the size of list ")
    size = int(input())

    print("Enter the list of numbers :")
    for i in range(size):
        no = int(input())
        listn.append(no)
    print("Input data is :",listn)

    Ret = list(filter(OddNumbers,listn))
    print("Odd Numbers are :",Ret)

if __name__ == "__main__":
    main()