def ChkNum(No):
    if (No > 1):
        print("Positive Number")
    elif (No <= -1):
        print("Negative Number")
    elif (No == 0):
        print("Zero")

def main():
    print("Enter the number")
    no = int(input())

    Ret = ChkNum(no)

if __name__ == "__main__":
    main()