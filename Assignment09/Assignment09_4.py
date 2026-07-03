def Cube(No1):
    Ans = No1 * No1 * No1
    return Ans

def main():
    data = int(input("Enter the number :"))
    Ret = Cube(data)
    print("Cube of", data, "Is :",Ret )

if __name__ == "__main__":
    main()
