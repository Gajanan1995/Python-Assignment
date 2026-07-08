def AdditionofElements(Data):
    sum = 0
    for i in Data:
        sum = sum + i 
    return sum

def main():
    Ldata = []

    print("Enther the number of elements")
    No1 = int(input())

    print("Enter the list of Numbers")
    for i in range(No1):
        no = int(input())
        Ldata.append(no)

    print(Ldata)

    Ret = AdditionofElements(Ldata)
    print("Addition of All Elements is",Ret)
if __name__ == "__main__":
    main()