Addition       = lambda No1,No2 : No1 + No2
Subtraction    = lambda No1,No2 : No1 - No2
Multiplication = lambda No1,No2 : No1 * No2
Division       = lambda No1,No2 : No1 / No2 

def main():
    print("Enter the first number : ")
    no1 = int(input())

    print("Enter the second number : ")
    no2 = int(input())

    Data0 = Addition(no1, no2)
    print(f"Addition of {no1} and {no2} is : {Data0}")

    Data1 = Subtraction(no1, no2)
    print(f"Subtraction of {no1} and {no2} is : {Data1}")

    Data2 = Multiplication(no1, no2)
    print(f"Multiplication of {no1} and {no2} is : {Data2}")

    Data3 = Division(no1, no2)
    print(f"Division of {no1} and {no2} is : {Data3 :.2f}")

if __name__ == "__main__":
    main()