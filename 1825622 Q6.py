import math

def main():
    # ask user for input of angle and lenght of adjacent
    theta = input("Enter the angle: ")
    adjacent = input("Enter the length of the adjacent side: ")
    
    # To accept only positive numbers
    if theta.isdigit() and adjacent.isdigit(): 
        theta = float(theta)
        adjacent = float(adjacent)
        
        # the angle should be less than 45
        if theta < 45:
            find_hypotenuse(theta,adjacent)
        else:
            print("Angle is out of range")
    else:
        print("Only positive integers")
        return
    
    
# a function to find the hypotenuse length
def find_hypotenuse(theta,adjacent):
    hypotenuse = adjacent / math.cos(math.radians(theta))
    print(f"Lenth of hypotenuse is: {hypotenuse:.3f}")
    return find_opposite(theta, hypotenuse)


# a function to find the opposite length
def find_opposite(theta,hypotenuse):
    opposite = math.sin(math.radians(theta)) * hypotenuse
    print(f"Length of opposite is :{opposite:.3f}")


# calling the main function to run the program 
if __name__ == "__main__":
    main()