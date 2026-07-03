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
    for Value in Result:
        print(Value, end=" ")

if __name__ == "__main__":
    main()