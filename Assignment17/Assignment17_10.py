def DigitCount(No):
    count = 0
    while(No != 0):
        count = count + No % 10
        No = No//10

    return count
def main():
    print("Enter the number")
    no = int(input())

    Ret = DigitCount(no)
    print(f"Addition of Digits {no} is:",Ret)
if __name__ == "__main__":
    main()