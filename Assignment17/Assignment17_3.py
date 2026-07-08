def factorial(Value):
    fact = 1
    for i in range(Value, 1, -1):
        fact = fact * i 
    return fact
def main():
    print("Enter the Number")
    no = int(input())

    Ret = factorial(no)
    
    print(f"factorial of {no} is : {Ret}")

if __name__ == "__main__":
    main()