def NaturalSum(Value):
    Sum = 0
    for i in range(1, Value+1):
        Sum = Sum + i 
    return Sum

def main():

    print("Enter the Number : ")
    number = int(input())

    Result = NaturalSum(number)

    print("Sum of N Natural Number is : ",Result)

if __name__ == "__main__":
    main()