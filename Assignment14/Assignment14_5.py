CheckEven = lambda no: (no % 2 == 0)

def main():
    no = int(input("Enter the number : "))
    Ret = CheckEven(no)

    print(Ret)

if __name__ == "__main__":
    main()