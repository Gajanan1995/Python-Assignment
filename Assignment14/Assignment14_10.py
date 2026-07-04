FindMax = lambda data: max(data)

def main():
    Maxnum = list()
    print("Enter three numbers ")
    el1 = int(input("Enter first number : "))
    Maxnum.append(el1)

    el1 = int(input("Enter second number : "))
    Maxnum.append(el1)

    el1 = int(input("Enter thrird number : "))
    Maxnum.append(el1)


    Result = FindMax(Maxnum)

    print("Maximum number is :",Result)

if __name__ == "__main__":
    main()