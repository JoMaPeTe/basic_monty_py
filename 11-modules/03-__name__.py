#LA variable __name__ es una variable especial en Python que 
# indica el nombre del módulo actual.
# Ayuda a controlar el comportamiento de un modulo cuando se
# esté importando o cuando se esté ejecutando directamente. 
# Cuando un módulo se ejecuta directamente, __name__ toma el 
# valor "__main__".

import my_module
#my_module.greet()
'''my_module has been imported
This is the my_module. This will always execute when the module is imported or run directly.'''
my_module.greet()
'''my_module has been imported
This is the my_module. This will always execute when the module is imported or run directly.
Hello from my_module!'''