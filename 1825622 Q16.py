import math

def main():
    try:
        # input of B,C and angle
        B_value = float(input("Enter the length of B: "))
        C_value = float(input("Enter the length of C: "))
        alpha = input("Enter the angle: ")
        # making sure the inputs are positive numbers
        if B_value > 0 and C_value > 0 and alpha.isdigit():
            alpha = float(alpha)
            # angle must be less than or equal to 90
            if alpha <= 90:
                findA(B_value,C_value,alpha)
            else:
                print("Angle is out of range")
        else:
            print("All inputs must be positive integers")
    # preventing an input of numbers
    except ValueError:
        print('Only numbers')
        

def  findA(B,C,alpha):
    # squareing the B and C
     B_sq = B ** 2
     C_sq = C ** 2 
    #  converting the degree to radians
     angle = math.radians(alpha)
    # applying the formular to calucute for A
     first_value = B_sq + C_sq -2 * B* C * math.cos(angle)
     final_value = math.sqrt(first_value)
    # print out the final answer in 2 decimal place
     print(f'Length of A is {final_value :.2f}')
     
# calling the main function to run the program
if __name__ == "__main__":
    main()