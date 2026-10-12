def listar_posts(lista):
    if not lista:
        print("No hay posts disponibles.")
        return

    print("\n--- TODOS LOS POSTS ---")

    for post in lista:
        print(f"\nTítulo: {post['titulo']}")
        print(f"Autor: {post['autor']['nombre']}")
        print(f"Estado: {post['estado']}")


def buscar_por_titulo(lista, termino):
    termino = termino.lower()
    encontrados = []

    for post in lista:
        if termino in post["titulo"].lower():
            encontrados.append(post)

    return encontrados


def filtrar_por_tag(lista, tag):
    tag = tag.lower()
    encontrados = []

    for post in lista:
        tags = [t.lower() for t in post["tags"]]

        if tag in tags:
            encontrados.append(post)

    return encontrados