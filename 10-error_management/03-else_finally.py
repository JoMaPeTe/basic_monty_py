def divide_numbers():
    try:
        a= int(input("Enter numerator: "))
        b= int(input("Enter denominator: "))
        result = a / b
 
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {type(e)}")
    else: #Si no hubo excepciones se ejecuta este bloque
        print(result)
        return result
    finally: #Se ejecuta siempre, haya o no excepciones
        print("Execution of divide_numbers is complete.")   
        
divide_numbers()
#try

#except