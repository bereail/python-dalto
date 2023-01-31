import re

email = "bereailsolohaga@hotmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]"


result = re.match(pattern, email)

if result:
    print("direccion de correo invalida")
else:
    print("direccion valida")