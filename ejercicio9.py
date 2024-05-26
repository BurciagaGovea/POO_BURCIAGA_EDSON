CorrectPass = "POO123"
UserPass = input(f"Ingresa la contraseña: ")
while UserPass != CorrectPass:
    UserPass = input(f"Ingresa la contraseña: ")
print(f"¡Contraseña correcta!")
