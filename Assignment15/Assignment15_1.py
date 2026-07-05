SquareofList = lambda List: List * List

def main():

    numlist = list()
    print("Enter the size of list")
    size = int(input())
    print("Enter the list of numbers ")
    for i in range(size):
        no = int(input())
        numlist.append(no)
    
    MData = list(map(SquareofList,numlist))
    print(MData)

if __name__ == "__main__":
    main()

