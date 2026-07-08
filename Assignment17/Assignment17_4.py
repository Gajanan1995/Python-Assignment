def SumofFactors(No):
    total = 0
    for i in range(1, No//2+1):
        if No % i == 0:
            total = total + i
    return total

def main():
    print("Enter the Number")
    no = int(input())

    Ret = SumofFactors(no)
    print("Addition of factor is :",Ret)

if __name__ == "__main__":
    main()