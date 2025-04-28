def validate_alpha(s):
    return s.isalpha()

input_str = "Hola Mundo"
if validate_alpha(input_str):
    print("Cadena válida.")
else:
    print("Cadena inválida.")