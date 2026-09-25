def validar_titulo(titulo):
    if not titulo.strip():
        return False, "O título é obrigatório."

    if len(titulo.strip()) < 2:
        return False, "O título deve possuir pelo menos 2 caracteres."

    return True, ""


def validar_categoria(categoria):
    categorias = [
        "Filme",
        "Série",
        "Livro",
        "Jogo"
    ]

    if categoria not in categorias:
        return False, "Selecione uma categoria válida."

    return True, ""


def validar_tipo(tipo):
    if not tipo.strip():
        return False, "Informe o gênero ou tipo da mídia."

    return True, ""


def validar_nota(nota):
    if not nota.strip():
        return False, "A nota é obrigatória."

    try:
        valor = float(nota)
    except ValueError:
        return False, "A nota deve ser um número."

    if valor < 0 or valor > 10:
        return False, "A nota deve estar entre 0 e 10."

    return True, ""


def validar_status(status):
    status_validos = [
        "Quero consumir",
        "Em andamento",
        "Concluído"
    ]

    if status not in status_validos:
        return False, "Selecione um status válido."

    return True, ""


def validar_midia(titulo, categoria, tipo, nota, status):
    validacoes = [
        validar_titulo(titulo),
        validar_categoria(categoria),
        validar_tipo(tipo),
        validar_nota(nota),
        validar_status(status)
    ]

    for valido, mensagem in validacoes:
        if not valido:
            return False, mensagem

    return True, ""