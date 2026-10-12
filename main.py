
from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def mostrar_resultados(lista):
    if not lista:
        print("No se encontraron posts.")
        return

    for post in lista:
        print(f"\nTítulo: {post['titulo']}")
        print(f"Autor: {post['autor']['nombre']}")
        print(f"Estado: {post['estado']}")


def ejecutar_programa():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)

        elif opcion == "2":
            termino = input("Ingrese el término a buscar: ")
            resultados = buscar_por_titulo(posts, termino)
            mostrar_resultados(resultados)

        elif opcion == "3":
            tag = input("Ingrese el tag a buscar: ")
            resultados = filtrar_por_tag(posts, tag)
            mostrar_resultados(resultados)

        elif opcion == "4":
            print("\n--- VALIDACIÓN DE POSTS ---")

            for post in posts:
                errores = validar_post(post)

                if not errores:
                    print(f"\n'{post['titulo']}' es válido.")
                else:
                    print(f"\n'{post['titulo']}' tiene errores:")

                    for error in errores:
                        print(f"- {error}")

        elif opcion == "5":
            print("\n¡Gracias por utilizar el sistema del blog!")
            print("Hasta luego.")
            break

        else:
            print("\nOpción inválida. Seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    ejecutar_programa()
