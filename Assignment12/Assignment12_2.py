def factors(Value):
    fact = []
    for i in range(1, Value + 1):
        if Value % i == 0:
            fact.append(i)
    return fact
            
def main():
    print("Enter the Number to get it's factor ")
    no = int(input())

    Rec = factors(no)
    for val in Rec:
        print(val, end=" ")

if __name__ == "__main__":
    main()