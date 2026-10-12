def validar_post(post):
    errores = []

    if not isinstance(post, dict):
        errores.append("El post no es un diccionario.")
        return errores

    claves_requeridas = [
        "titulo",
        "contenido",
        "autor",
        "tags",
        "estado"
    ]

    for clave in claves_requeridas:
        if clave not in post:
            errores.append(f"Falta la clave '{clave}'.")

    if "titulo" in post:
        if not isinstance(post["titulo"], str) or not post["titulo"].strip():
            errores.append("El título no puede estar vacío.")

    if "contenido" in post:
        if not isinstance(post["contenido"], str) or not post["contenido"].strip():
            errores.append("El contenido no puede estar vacío.")

    if "autor" in post:
        if not isinstance(post["autor"], dict):
            errores.append("El autor debe ser un diccionario.")
        else:
            if "nombre" not in post["autor"]:
                errores.append("El autor debe tener un nombre.")
            elif not isinstance(post["autor"]["nombre"], str) or not post["autor"]["nombre"].strip():
                errores.append("El nombre del autor no puede estar vacío.")

    if "tags" in post:
        if not isinstance(post["tags"], list):
            errores.append("Los tags deben estar guardados como lista.")

    if "estado" in post:
        estados_validos = {
            "borrador",
            "publicado",
            "archivado"
        }

        if post["estado"] not in estados_validos:
            errores.append("El estado del post no es válido.")

    return errores