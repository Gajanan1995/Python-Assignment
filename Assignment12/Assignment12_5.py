def CountNo(Value):
    count = []
    for i in range(Value, 0, -1):
        count.append(i) 
    return count

def main():

    print("Enter the number : ")
    no = int(input())
    Ret = CountNo(no)

    for val in Ret:
        print(val, end=" ")

if __name__ == "__main__":
    main()