###############################################################################
# CALCULATOR
###############################################################################


while True:

    select = input("Select the function what you want (ex: add, multi, sub, divs): ")
    
    if select == "stop":
        break
    
    num_1 = int(input("Enter the 1st number: "))
    num_2 = int(input("Enter the 2nd number: "))
    
    add = num_1 + num_2
    multi = num_1*num_2
    sub = num_1-num_2
    divs = num_1/num_2

    def calculator(num_1, num_2, select):
   
        if select == "add":
            print("addition: ", add)
    
        elif select == "multi":
            print("multiple: ", multi)
        
        elif select == "sub":
            print("subtraction: ", sub)
            
        elif select == "divs":
            print("division: ", divs)
            
        else:
            print("Error! You selected the undefined function!") 
            

    calculator(num_1, num_2, select)
