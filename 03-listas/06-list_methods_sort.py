letters=['d', 'a', 'c', 'b', 'e']
print(letters)
""" letters.sort()
print(letters) """

#sorted function
""" new_letters= sorted(letters, reverse=True)
print(new_letters)
print(letters)

new_letters2= new_letters[:]
new_letters2.sort()
print(new_letters)
print(new_letters2) """

new_letters3 = letters.copy()
new_letters3.sort()
print(letters)
print(new_letters3)


letters.reverse()
print(letters)