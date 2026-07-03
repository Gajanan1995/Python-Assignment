def Square(No1):
    Ans = No1 * No1
    return Ans

def main():
    Value = int(input("Enter the Number :"))
    Res = Square(Value)

    print(f"Square of", Value, "is", Res)

if __name__ == "__main__":
    main()