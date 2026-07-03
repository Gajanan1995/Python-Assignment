def EvenNumber(No):
    data = []
    for i in range(1, No+1):
        if (i % 2 == 0):
            data.append(i)
    return data 

def main():
    print("Enter the Number : ")

    no = int(input())

    Result = EvenNumber(no)
    print(f"Even Number till {no} is",Result)

if __name__ == "__main__":
    main()