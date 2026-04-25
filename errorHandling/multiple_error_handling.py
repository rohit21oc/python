my_list = [1, 2, 3, 4, 5]
 # This will raise a ZeroDivisionError

try:
    print(my_list[0])
    print(10 / 0) 
    print(my_list[10])
    print(my_list[3])
    print(my_list[4])
    
except IndexError:
    print("An error occurred while trying to access the list element.")
except ZeroDivisionError:
    print("An error occurred while trying to divide by zero.")  
else:
    print("Everything went well, no errors occurred.")
