def MaxNumber(Data):
    Max = Data[0]
    for i in Data:
        if i > Max:
            Max = i 
    return Max

def main():
    Ldata = []

    print("Enther the number of elements")
    No1 = int(input())

    print("Enter the list of Numbers")
    for i in range(No1):
        no = int(input())
        Ldata.append(no)

    print(Ldata)

    Ret = MaxNumber(Ldata)
    print("Maximum number is",Ret)
if __name__ == "__main__":
    main()