def big_function(*args, **kwargs):
    '''
    Docstring for big_function
    
    :param args: we don't know how many arguments will be passed
    :param kwargs: we don't know how many keyword arguments will be passed
    '''
    print("Arguments:", args) #print positional arguments as a tuple
    print("Keyword Arguments:", kwargs) #print keyword arguments as a dictionary    
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total  #return the sum of all positional arguments and keyword arguments
# Example usage
print(big_function(1,2))  # Passing only positional arguments #(1, 2)
print(big_function(1,2,3,4,5,6))  # Passing multiple positional argument

print(big_function( 2,  num2=2, age=30, num1=100))  # Passing both positional and keyword arguments