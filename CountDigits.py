def CountDigits(value):
    Data = len(value)
    return Data

def main():

    print("Enter the Number : ")
    No1 = input()
    Ret = CountDigits(No1)
    print("Number of Digits is : ",Ret)

if __name__ == "__main__":
    main()