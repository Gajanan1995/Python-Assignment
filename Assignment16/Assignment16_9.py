def EvenNum():
    even = []
    for i in range(1, 21):
        if i % 2 == 0:
            even.append(i)
    return even
def main():
    print("First 10 Even Numbers are : ")
    Ret = EvenNum()
    print(Ret, end=" ")

if __name__ == "__main__":
    main()