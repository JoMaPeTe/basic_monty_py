def greet():
    print("Hello from my_module!")

if __name__ == "__main__":
    print("my_module is being run directly")
    greet()
else:
    print("my_module has been imported")

print("This is the my_module. This will always execute when the module is imported or run directly.")


''' py my_module.py
my_module is being run directly
Hello from my_module!
This is the my_module. This will always execute when the module is imported or run directly.
'''