from colorama import init, Fore, Style, Back
init()

# registro()
# Diccionario para almacenar los usuarios
usuarios = {}

def registrar_usu():
    """Función para registrar un nuevo usuario"""
    while True:
        usu = input("Ingrese el nombre de usuario o escriba Menu para volver:  ").strip().upper()
        if usu == "MENU" or usu =="MENÚ":
            main()
        if not usu:
            print("El nombre de usuario no puede estar vacío. {Fore.RED}Intente de nuevo.{Style.RESET_ALL}")
            continue
        if usu in usuarios:
            print("Este nombre de usuario ya está en uso. Por favor, elija otro.")
        else:
            contra = input("Ingrese la contraseña: ")
            if not contra:
                print("La contraseña no puede estar vacía. {Fore.RED}Intente de nuevo.{Style.RESET_ALL}")
                continue
            usuarios[usu] = contra
            print("{Fore.GREEN}Usuario registrado exitosamente.{Style.RESET_ALL}")
            return

def logueo():
    """Función para iniciar sesión"""
    # if len(usuarios) == 0:
    #         print("No hay registros que Borrar")
    #         main()
    #else:
    while True:
            usu = input("Ingrese el nombre de usuario o escriba Menu para volver: ").upper()
            if usu == "MENU" or usu =="MENÚ":
               main()
            if usu not in usuarios:
                print(f"{Back.RED}El nombre de usuario no existe. Por favor, regístrese primero.{Style.RESET_ALL}")
            else:
                contra = input("Ingrese la contraseña: ")
                if usuarios[usu] == contra:
                    print("Inicio de sesión exitoso.")
                    return
                else:
                    print("Contraseña incorrecta. Intente de nuevo.")

def borrar_usu():
    """Función para eliminar usuario"""
    if len(usuarios) == 0:
            print("No hay registros que Borrar")
            main()
    else:
            while True:
                usu = input("Ingrese el nombre de usuario o escriba Menu para volver: ").upper()
                if usu == "MENU" or usu =="MENÚ":
                    main()
                if usu not in usuarios:
                    print("El nombre de usuario no existe. Por favor, repita búsqueda.")
                else:
                    contra = input("Ingrese su contraseña actual: ")
                    if usuarios[usu] == contra:
                        del usuarios[usu]
                        print(f"El usuario '{usu}' ha sido eliminado exitosamente.")
                        return
                    else:
                        print("Contraseña incorrecta. Intente de nuevo.")
                    
def mostrar():
    """Función para mostrar registros"""
    if not usuarios:
        print("No hay Usuarios registrados.")
        main()
    else:
        for usu, contra in usuarios.items():
            print("*" * 25)
            print(f"- Nombre de usuario: {usu}")
            print(f"  Contraseña: {contra}")
            print("*" * 40)
        print()
    
def main():
    """Función principal del programa"""
    
    while True:
            print()
            print("*" * 45)
            print(f"{Back.CYAN}{Fore.BLACK}Menú Registro de Usuarios --> CoderHouse <--{Style.RESET_ALL}")
            print("*" * 45)
            print(f"{Fore.YELLOW}>> 1 <<{Style.RESET_ALL} AGREGAR  USUARIO")
            print(f"{Fore.YELLOW}>> 2 <<{Style.RESET_ALL} ELIMINAR USUARIO")
            print(f"{Fore.YELLOW}>> 3 <<{Style.RESET_ALL} INGRESAR")
            print(f"{Fore.YELLOW}>> 4 <<{Style.RESET_ALL} MOSTRAR  USUARIOS")
            print(f"{Fore.RED}>> 5 <<{Style.RESET_ALL} Bye-bye")

            opcion = input("Ingrese la opción deseada (1-5): ")

            if opcion == "1":
                registrar_usu()
            elif opcion == "2":
                borrar_usu()
            elif opcion == "3":
                logueo()
            elif opcion == "4":
                mostrar()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")    

if __name__ == "__main__":
    main()
    
