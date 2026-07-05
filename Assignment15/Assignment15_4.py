from functools import reduce

Addition = lambda No1, No2: No1 + No2

def main():
    print("Enter the size of list ")
    size = int(input())

    data = []
    print("Enter the numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    Rdata = reduce(Addition,data)
    print("Addition of list is : ",Rdata)
if __name__ == "__main__":
    main()