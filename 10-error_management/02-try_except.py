def divide_numbers():
    try:
        a= int(input("Enter numerator: "))
        b= int(input("Enter denominator: "))
        result = a / b
        print(result)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {type(e)}")
    
divide_numbers()
#try

#except