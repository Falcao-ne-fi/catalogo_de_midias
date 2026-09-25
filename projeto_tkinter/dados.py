import sqlite3


NOME_BANCO = "catalogo_midias.db"


def conectar():
    return sqlite3.connect(NOME_BANCO)


def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS midias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            tipo TEXT NOT NULL,
            nota REAL NOT NULL,
            status TEXT NOT NULL,
            observacao TEXT
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_midia(titulo, categoria, tipo, nota, status, observacao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO midias
        (titulo, categoria, tipo, nota, status, observacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        titulo,
        categoria,
        tipo,
        nota,
        status,
        observacao
    ))

    conexao.commit()
    conexao.close()


def listar_midias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, categoria, tipo, nota, status, observacao
        FROM midias
        ORDER BY titulo
    """)

    registros = cursor.fetchall()

    conexao.close()

    return registros


def pesquisar_midias(termo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, categoria, tipo, nota, status, observacao
        FROM midias
        WHERE titulo LIKE ?
           OR categoria LIKE ?
           OR tipo LIKE ?
           OR status LIKE ?
        ORDER BY titulo
    """, (
        f"%{termo}%",
        f"%{termo}%",
        f"%{termo}%",
        f"%{termo}%"
    ))

    registros = cursor.fetchall()

    conexao.close()

    return registros


def buscar_midia(id_midia):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, categoria, tipo, nota, status, observacao
        FROM midias
        WHERE id = ?
    """, (id_midia,))

    registro = cursor.fetchone()

    conexao.close()

    return registro


def editar_midia(
    id_midia,
    titulo,
    categoria,
    tipo,
    nota,
    status,
    observacao
):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE midias
        SET titulo = ?,
            categoria = ?,
            tipo = ?,
            nota = ?,
            status = ?,
            observacao = ?
        WHERE id = ?
    """, (
        titulo,
        categoria,
        tipo,
        nota,
        status,
        observacao,
        id_midia
    ))

    conexao.commit()
    conexao.close()


def excluir_midia(id_midia):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM midias
        WHERE id = ?
    """, (id_midia,))

    conexao.commit()
    conexao.close()


def obter_resumo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM midias
    """)
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM midias
        WHERE status = 'Concluído'
    """)
    concluidos = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM midias
        WHERE status = 'Em andamento'
    """)
    andamento = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM midias
        WHERE status = 'Quero consumir'
    """)
    quero = cursor.fetchone()[0]

    cursor.execute("""
        SELECT AVG(nota)
        FROM midias
    """)
    media = cursor.fetchone()[0]

    conexao.close()

    if media is None:
        media = 0

    return {
        "total": total,
        "concluidos": concluidos,
        "andamento": andamento,
        "quero": quero,
        "media": media
    }