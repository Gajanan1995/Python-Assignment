FindMim = lambda data: min(data)

def main():
    Minnum = list()
    print("Enter five elements ")
    el1 = int(input("Enter first elements : "))
    Minnum.append(el1)

    el1 = int(input("Enter second elements : "))
    Minnum.append(el1)

    el1 = int(input("Enter thrir elements : "))
    Minnum.append(el1)

    el1 = int(input("Enter fourth elements : "))
    Minnum.append(el1)

    el1 = int(input("Enter fifth elements : "))
    Minnum.append(el1)

    Result = FindMim(Minnum)

    print("Minimum number is :",Result)

if __name__ == "__main__":
    main()