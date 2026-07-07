def ChkNum(No):
    if (No % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter the number :")
    no = int(input())

    Ret = ChkNum(no)

    if (Ret == True):
        print(f"{no} Even Number")
    else:
        print(f"{no} Odd Number")

if __name__ == "__main__":
    main()