def Factorial(Value1):

    for i in range(Value1):
        Fact = i - Value1
    return Fact

def main():
    print("Enter the number :")
    No1 = int(input())

    Ret = Factorial(No1)

    print("Factorial is :", Ret)

if __name__ == "__main__":
    main()
