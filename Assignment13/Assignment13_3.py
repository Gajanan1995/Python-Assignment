def PerfectNumber(Value):

    perfect = 0

    if Value <= 1:
        return False 
    
    for no in range(1, (Value // 2) + 1):
        if Value % no == 0:
            perfect += no
    return perfect == Value



def main():
    print("Enter the number : ")
    no = int(input())

    Ret = PerfectNumber(no)
    if Ret == True:
        print(f"{no} Is perfect Number ")
    else:
        print(f"{no} Is not a perfect number")

if __name__ == "__main__":
    main()