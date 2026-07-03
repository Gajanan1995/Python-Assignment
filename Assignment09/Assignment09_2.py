def ChkGreater(Value1, Value2):
    if Value1 > Value2:
        return Value1
    else:
        return Value2

def main():
    No1 = int(input("Enter the First Number :"))
    No2 = int(input("Enter the Second Number : "))

    Ret = ChkGreater(No1, No2)
    print("Greater Number is: ",Ret)

if __name__ == "__main__":
    main()