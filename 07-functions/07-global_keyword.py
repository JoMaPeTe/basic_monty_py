tax = 16
def change_global_wrong():
    tax = 8  # This creates a new local variable 'tax', doesn't modify the global one
    return tax

print("Before change_global_wrong, tax =", tax)
print(change_global_wrong())  # This will print 8, but won't change the global variable
print("After change_global_wrong, tax =", tax)

def change_global_correct():
    global tax
    tax = 8  # This modifies the global variable 'tax'
    return tax

print("Before change_global_correct, tax =", tax)
print(change_global_correct())  # This will print 8, and will change the global variable
print("After change_global_correct, tax =", tax)