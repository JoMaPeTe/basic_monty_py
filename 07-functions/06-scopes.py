global_variable = "I am global"
def outer_function():
    enclosed_variable = "I am enclosed"
    def inner_function():
        local_variable = "I am local"
        print(global_variable)
        print(enclosed_variable)
        print(local_variable)
    inner_function()
    #print(local_variable) it won't work
outer_function()