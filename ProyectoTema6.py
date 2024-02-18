from pathlib import Path
import os

def welcome_message():
    print("¡Bienvenido a la Oficina Virtual!")
    print("-------------------------------")

def show_directory_info(directory_path):
    print(f"Directorio actual: {directory_path}")
    total_registros = count_records(directory_path)
    print(f"Total de registros en la carpeta: {total_registros}")
    print("-------------------------------")

def count_records(directory_path):
    total_registros = 0
    for subdir, _, _ in os.walk(directory_path):
        total_registros += len([name for name in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, name))])
    return total_registros

def print_menu():
    print("Menú Principal:")
    print("1. Leer documento")
    print("2. Crear documento")
    print("3. Crear categoría")
    print("4. Eliminar documento")
    print("5. Eliminar categoría")
    print("6. Salir")
    print("-------------------------------")

def get_user_choice():
    return input("Seleccione una opción (1-6): ")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_document(category, document):
    file_path = Path(f"./Oficina/{category}/{document}.txt")
    if file_path.exists():
        with open(file_path, "r") as file:
            content = file.read()
            print(f"\nContenido de {document}.txt:\n{content}")
    else:
        print(f"\nEl documento {document}.txt no existe.")
    input("\nPresiona Enter para volver al menú principal...")

def create_document(category, document_name, document_content):
    file_path = Path(f"./Oficina/{category}/{document_name}.txt")
    with open(file_path, "w") as file:
        file.write(document_content)
        print(f"\n¡Documento {document_name}.txt creado con éxito!")
    input("\nPresiona Enter para volver al menú principal...")

def create_category(category_name):
    category_path = Path(f"./Oficina/{category_name}")
    category_path.mkdir(exist_ok=True)
    print(f"\n¡Categoría {category_name} creada con éxito!")
    input("\nPresiona Enter para volver al menú principal...")

def delete_document(category, document_name):
    file_path = Path(f"./Oficina/{category}/{document_name}.txt")
    if file_path.exists():
        file_path.unlink()
        print(f"\n¡Documento {document_name}.txt eliminado con éxito!")
    else:
        print(f"\nEl documento {document_name}.txt no existe.")
    input("\nPresiona Enter para volver al menú principal...")

def delete_category(category_name):
    category_path = Path(f"./Oficina/{category_name}")
    if category_path.exists():
        category_path.rmdir()
        print(f"\n¡Categoría {category_name} eliminada con éxito!")
    else:
        print(f"\nLa categoría {category_name} no existe.")
    input("\nPresiona Enter para volver al menú principal...")

# Función principal
def main():
    directory_path = Path("./Oficina")
    welcome_message()

    while True:
        clear_console()
        show_directory_info(directory_path)
        print_menu()
        user_choice = get_user_choice()

        if user_choice == "1":
            category = input("Ingrese la categoría del documento: ")
            document = input("Ingrese el nombre del documento: ")
            read_document(category, document)

        elif user_choice == "2":
            category = input("Ingrese la categoría del nuevo documento: ")
            document_name = input("Ingrese el nombre del nuevo documento: ")
            document_content = input("Ingrese el contenido del nuevo documento: ")
            create_document(category, document_name, document_content)

        elif user_choice == "3":
            category_name = input("Ingrese el nombre de la nueva categoría: ")
            create_category(category_name)

        elif user_choice == "4":
            category = input("Ingrese la categoría del documento a eliminar: ")
            document = input("Ingrese el nombre del documento a eliminar: ")
            delete_document(category, document)

        elif user_choice == "5":
            category_name = input("Ingrese el nombre de la categoría a eliminar: ")
            delete_category(category_name)

        elif user_choice == "6":
            print("\n¡Gracias por usar la Oficina Virtual! Hasta luego.")
            break

        else:
            input("\nOpción no válida. Presiona Enter para volver al menú principal...")

main()
