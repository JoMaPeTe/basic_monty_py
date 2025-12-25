#To handle text files in Python, you don't need to install any external libraries. 
# You can use the built-in open() function to read from and write to
# files. Here's a simple example of how to create, write to, 
# and read from a text file:
# Wherever you open a file, make sure to close it after you're done
# to free up system resources.

#my_file = open("example.txt", "w")  # Open a file in write mode
my_file = open("example.txt")
# print(my_file.read())
# print(my_file.read())
# print(my_file.read())
# Seek, value in bytes where you want to go in the file
# my_file.seek(4)
# print(my_file.read())

# readline reads a single line from the file

print(my_file.readline(3))  # Read the first line (up to 30 characters)
print(my_file.readline())  # Read the second line
print(my_file.readline())
print(my_file.readline())
print(my_file.readlines())
'''
Hol
a

Mundo

How are you doing?

['Richi\n', 'Gati\n', 'Perry\n', '123\\\n', '>:)']
'''
my_file.close()