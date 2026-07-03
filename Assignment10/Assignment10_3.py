def Factorial(No):
    Fact = 1
    for i in range(1, No+1):
        Fact = Fact * i 
    return Fact

def main():

    print("Enter the Number : ")
    Value = int(input())

    data = Factorial(Value)
    print(f"Factorial of {Value} is :",data)

if __name__ == "__main__":
    main()