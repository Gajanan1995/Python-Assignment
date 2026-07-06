Stringx = lambda str1: len(str1) > 5

def main():
    print("Enter the size of list")
    size = int(input())

    strlist = []
    print("Enter the strings: ")
    for i in range(size):
        no = input()
        strlist.append(no)

    Fdata = list(filter(Stringx, strlist))

    print("String which are greater then five :",Fdata)


if __name__ == "__main__":
    main()