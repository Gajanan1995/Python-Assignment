def ReverseNumbers(Value):
    Reverse = 0 
    while (Value != 0):
        extract = Value % 10 
        Reverse = (Reverse * 10) + extract 
        Value = Value // 10 
    return Reverse

def main():

    print("Enter the Number : ")
    Data = int(input())
    result = ReverseNumbers(Data)
    print(result)

if __name__ == "__main__":
    main()