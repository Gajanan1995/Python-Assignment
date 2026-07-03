def CheckDivisible(No1):
    if No1  % 3 == 0 and No1 % 5 == 0:
        return True
    else:
        return False

def main():
    
    Value = int(input("Enter the Number : "))
    Ret = CheckDivisible(Value)

    if(Ret == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

if __name__ == "__main__":
    main()