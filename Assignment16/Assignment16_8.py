def Star(Value):
    for i in range(Value):
        print("*", end=" ")

def main():
    print("Enter the Number")
    no = int(input())
    Star(no)

if __name__ == "__main__":
    main()