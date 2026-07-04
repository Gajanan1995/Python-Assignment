Cubeof = lambda No: No * No * No

def main():
    no = int(input("Enter the number : "))
    Ndata = Cubeof(no)
    print(f"Cube of {no} is : {Ndata}")
if __name__ == "__main__":
    main()