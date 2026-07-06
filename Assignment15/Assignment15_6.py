from functools import reduce

MinNumber = lambda No1, No2: min(No1, No2)

def main():
    listdata = []
    print("Enter the size of list")
    size = int(input())

    print("Enter the numbers :")

    for i in range(size):
        no = int(input())
        listdata.append(no)

    Result = reduce(MinNumber,listdata)

    print(f"Provided numbers {listdata}")
    print("Minimum number is :",Result)

if __name__ == "__main__":
    main()