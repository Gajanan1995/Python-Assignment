def PrimeNumber(Data):
    if Data <= 1:
        return False
    for i in range(2, Data):
        if Data % i == 0:
            return False
    return True

def main():
    No1 = int(input("Enter the number : "))

    Ret = PrimeNumber(No1)
    if (Ret == True):
        print("It's Prime Number")
    else:
        print("It's Not Prime Number")

if __name__ == "__main__":
    main()