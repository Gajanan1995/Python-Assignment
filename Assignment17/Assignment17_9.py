def DigitCount(No):
    count = 0
    while(No != 0):
        No = No//10
        count = count+1
    return count
def main():
    print("Enter the number")
    no = int(input())

    Ret = DigitCount(no)
    print(f"Number of Digit in {no} is:",Ret)
if __name__ == "__main__":
    main()