import math

def main():
        # accepts inputs form user
        a= float(input("Enter the value for a: "))
        b = float(input("Enter the value for b: "))
        c = float(input("Enter the value for c: "))
        
        # accetps only positve integers
        if a > 0 and b > 0 and c > 0:
            
            # checks for value error 
            try:
                checker = math.log(b**2 -3*a*c)
                # checks if the variable checker is greater or equal to 0.5
                
                if checker >= 0.5:
                    print("We are good to go")
                    functEquation1(a,b,c)
                    functEquation2(a,b,c)
                else:
                    print("Let's call it a day")
            except ValueError:
                
                print("Let's call it a day")
                return
            

def functEquation1(a,b,c):
    # calculates for the result using the formular
    solution = (-b + math.log(b**2 -3*a*c)) / math.log(2*c)
    print(f'The solution is  for  equation1{solution}')


def functEquation2(a,b,c):
    # calculates for the seconde result using the second formular
    solution = (-b - math.log(b**2 -3*a*c)) / math.log(2*c)
    print(f'Solution is  for equation2 {solution}')
    
    # calls out the main function and runs the program
if __name__ == "__main__":
    main()