def DisplayPattern(Value):
    for i in range(Value, 0, -1):
        for j in range(i):
            print("*",end=" ")
        print()
    
def main():
    print("Enter the number")
    no = int(input())
    DisplayPattern(no)
if __name__ == "__main__":
    main()