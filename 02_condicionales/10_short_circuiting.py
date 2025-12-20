#Corto Circuito
#OR solo necesita un True y no evalúa el segundo operando
True or print("Esto no se imprime porque el primer operando es True")
False or print("Esto se imprime porque el primer operando es False")

#AND solo necesita un False y no evalúa el segundo operando
False and print("Esto no se imprime porque el primer operando es False")
True and print("Esto se imprime porque el primer operando es True")

#Ejemplo práctico
#name = "Alice"
name = None
print( name and name.upper())  # Como el primer operando es None, no se evalúa el segundo operando y el resultado es None, evitando un error al tratar de aplicar un metodo de string.