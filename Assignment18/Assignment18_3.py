def MinimumNumber(Data):
    Minimum = Data[0]
    for value in Data:
        if value < Minimum:
            Minimum = value 
    return Minimum

def main():
    Ldata = []

    print("Enther the number of elements")
    No1 = int(input())

    print("Enter the list of Numbers")
    for i in range(No1):
        no = int(input())
        Ldata.append(no)

    print(Ldata)

    Ret = MinimumNumber(Ldata)
    print("Minimum number is",Ret)
if __name__ == "__main__":
    main()