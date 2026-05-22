manager = []

while True:

    opciones = 0

    if opciones < 6:
    
        print()
        print("===========================================")
        print("Seleccione alguna de las opciones del menú")
        print("===========================================")
        print()
        print("1. Nueva contraseña.")
        print("2. Editar contraseña.")
        print("3. Eliminar contraseña.")
        print("4. Ver contraseña.")
        print("5. Buscar contraseña.")
        
        menu = input("Elija una opción")
        
    match menu:
        case "1":
            
            print("======================")
            print("Nueva contraseña.")
            print("======================")
            
            pregunta = input("¿Desea crear una nueva contraseña? (Escriba 'Si' para continuar o 'No' para salir)").strip().title()
            
            if pregunta == "Si":
                
                print("Paso 1: Ingrese el nombre de la cuenta")
                account = input("Ingrese el nombre de la cuenta: ").strip().title()
                
                print("Paso 1: Ingrese el mail del usuario")
                user = input("Ingrese mail o nombre de usuario: ").strip().title()
                
                print("Paso 1: Ingrese la contreaseña del usuario")
                password = input("Ingrese su contraseña (Debe contener solo números): ")
                
                if account == "" or user == "" or password == "":
                    print("No ingresaste ningun dato...")
                    continue
                
                manager.append(user)
                manager.append(account)
                manager.append(password)
                print("¡Credencial guardada con éxito!")
            
            else:
                print("Operación cancelada.")
                
        case "2":
            
            print("======================")
            print("Editar contraseña.")
            print("======================")
            
        case "3":
            
            print("======================")
            print("Eliminar contraseña.")
            print("======================")
            
        case "4":
            
            print("======================")
            print("Ver contraseña.")
            print("======================")
            
        case "5":
            
            print("======================")
            print("Buscar contraseña.")
            print("======================")
            
        case  _:
            print("Opción incorrecta")
            
            
            
print("=====================================")
print("Sistema para gestion de contraseñas")
print("=====================================")