value=100 
 # value= 100 + 'Hola' Esto peta. No se puede sumar int y str
type_value=type(value)
print(f"El valor es {value} y su tipo es {type_value}")
# --- Int a Str ---
value=str(value)
type_value=type(value)
print(f"El valor es {value} y su tipo es {type_value}")
# --- Str a Int ---
value=int('100')
type_value=type(value)
print(f"El valor es {value} y su tipo es {type_value}")
# --- Str a Float ---
value=float('100.5')
type_value=type(value)
print(f"El valor es {value} y su tipo es {type_value}")
#value=float('Hola')  # Esto peta. No se puede convertir 'Hola' a float
value=float(100)
type_value=type(value)
print(f"El valor es {value} y su tipo es {type_value}")