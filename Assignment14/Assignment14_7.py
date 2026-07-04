isDivisible = lambda No: No % 5 ==0 

def main():

    no = int(input("Enter the number : "))
    Ret = isDivisible(no)
    print(Ret)
    
if __name__ == "__main__":
    main()