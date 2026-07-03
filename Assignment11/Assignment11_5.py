def palindrome(Value):
    Pal = 0 
    while(Value > 0):
        data = Value % 10
        Pal = (Pal * 10 ) + data
        Value = Value // 10 
    return Pal


def main():
    print("Enter the Number : ")
    No = int(input())

    Ans = palindrome(No)
    print(Ans)

if __name__ == "__main__":
    main()