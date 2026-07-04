Maxnum = lambda No1, No2: max(No1, No2) 
def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))

    Ret = Maxnum(no1, no2)
    print("Maximum number is",Ret)

if __name__ == "__main__":
    main()