def Multiplication(Value):
    Table = []
    for i in range(1, 11):
        Table.append(Value * i) 
    return Table

def main():

    print("Enter the Number :")
    No1 = int(input())
    Ret = Multiplication(No1)
    print(Ret)

if __name__ == "__main__":
    main()
