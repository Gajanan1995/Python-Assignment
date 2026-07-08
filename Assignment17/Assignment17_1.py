import Arithmetic

def main():
    print("Enter tow Numbers")

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    add = Arithmetic.Add(no1, no2)
    print(f"Addition of {no1}, {no2} is : {add}")

    sub = Arithmetic.Sub(no1, no2)
    print(f"Subtraction of {no1}, {no2} is : {sub}")

    multi = Arithmetic.Mult(no1, no2)
    print(f"multiplication of {no1}, {no2} is : {multi}")

    divi = Arithmetic.Div(no1, no2)
    print(f"Division of {no1}, {no2} is : {divi:.2f}")

if __name__ == "__main__":
    main()