def EvenNumber(No):
    for i in range(1, No+1):
        if (i % 2 == 0):
            print(i, end=" ")
def main():
    print("Enter the Number : ")
    no = int(input())
    EvenNumber(no)

if __name__ == "__main__":
    main()