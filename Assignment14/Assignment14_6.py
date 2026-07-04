CheckOdd = lambda No: (No % 2 != 0 )

def main():
    val = int(input("Enter the number : "))
    Ret = CheckOdd(val)

    print(Ret)

if __name__ == "__main__":
    main()