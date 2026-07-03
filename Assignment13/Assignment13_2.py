def Area(rad):
    PI = 3.14
    area = PI*rad*rad
    return area

def main():
    print("Enter the radius of circle :")

    radius = float(input())

    Ret = Area(radius)
    print(f"Area of Circle is : {Ret:.2f}")

if __name__ == "__main__":
    main()
