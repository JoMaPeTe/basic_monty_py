def outer():
    enclosed_var = "Enclosed"
    def inner():
        #nonlocal enclosed_var
        enclosed_var = "Modified Enclosed"
    inner()
    print("outer:", enclosed_var)
outer()  # This will print: outer: Enclosed

def outer2():
    enclosed_var = "Enclosed2"
    def inner():
        nonlocal enclosed_var
        enclosed_var = "Modified Enclosed2"
    inner()
    print("outer:", enclosed_var)
outer2()  # This will print: outer: Enclosed