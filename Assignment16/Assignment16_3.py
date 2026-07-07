def Add(No1, No2):
    Sum = 0 
    Sum = No1 + No2
    return Sum

def main():
    print("Enter the first number")
    no1 = int(input())

    print("Enther the second number")
    no2 = int(input())

    Ans = Add(no1, no2)
    print(f"Addition of two numbers {no1}, {no2} is : {Ans}")

if __name__ == "__main__":
    main()