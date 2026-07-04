multiplication = lambda No1, No2: No1 * No2

def main():
    print("Enter two number ")
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    Ret = multiplication(no1, no2)

    print("Multiplication of two number is :",Ret)

if __name__ == "__main__":
    main()