from functools import reduce

MaxNum = lambda No1, No2: max(No1, No2)
def main():
    print("Enter the size of list ")
    size = int(input())

    data = []
    print("Enther the list of numbers ")
    for i in range(size):
        no = int(input())
        data.append(no)

    Rdata = reduce(MaxNum,data)
    print("Maximum number is :",Rdata)

if __name__ == "__main__":
    main()