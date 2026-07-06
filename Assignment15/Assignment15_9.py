from functools import reduce

Product = lambda No1, No2: No1*No2

def main():
    print("Enter the size of list")
    size = int(input())

    print("Enter the elements :")

    numlist = []
    for i in range(size):
        no = int(input())
        numlist.append(no)

    Rdata = reduce(Product,numlist)

    print("Provided Elements ",numlist)
    print("Product of list is :",Rdata)

if __name__ == "__main__":
    main()