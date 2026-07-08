def ChkPrime(No):
    if No <= 1:
        return False
    
    for i in range(2, No):
        if No % i ==0:
            return False
    return True
        
def main():
    print("Enter the number")
    no = int(input())
    
    Ret = ChkPrime(no)

    if(Ret == True):
        print("It's Prime Number")
    else:
        print("It's not prime number")
if __name__ == "__main__":
    main()