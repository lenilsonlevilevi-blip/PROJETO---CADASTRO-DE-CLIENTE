import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "loja.db")

def conectar():
    print("Conectando em:", DB_PATH)
    return sqlite3.connect(DB_PATH)

# =========================
# CONEXÃO COM BANCO
# =========================
def conectar():
    return sqlite3.connect("loja.db")


# =========================
# CRIAR TABELA
# =========================
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        idade INTEGER,
        endereco TEXT,
        valor_compra REAL,
        data_compra TEXT
    )
    """)

    conn.commit()
    conn.close()


# =========================
# CADASTRAR CLIENTE
# =========================
def cadastrar_cliente():
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")
    valor_compra = float(input("Valor da compra: "))
    data_compra = input("Data da compra: ")

    cursor.execute("""
    INSERT INTO clientes (nome, telefone, idade, endereco, valor_compra, data_compra)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, telefone, idade, endereco, valor_compra, data_compra))

    conn.commit()
    conn.close()

    print("✅ Cliente cadastrado com sucesso!")


# =========================
# LISTAR CLIENTES
# =========================
def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    print("\n=== CLIENTES CADASTRADOS ===")
    for c in clientes:
        print(f"""
ID: {c[0]}
Nome: {c[1]}
Telefone: {c[2]}
Idade: {c[3]}
Endereço: {c[4]}
Valor da compra: R${c[5]}
Data da compra: {c[6]}
-----------------------------""")

    conn.close()
    input("\n Pressione Enter para continuar...")


# =========================
# DELETAR CLIENTE
# =========================
def deletar_cliente():
    conn = conectar()
    cursor = conn.cursor()

    id_cliente = int(input("Digite o ID do cliente para deletar: "))

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    conn.close()

    print(" 🗑️ Cliente removido!")


# =========================
# MENU PRINCIPAL
# =========================
def menu():
    criar_tabela()

    while True:
        print("\n=== SISTEMA DA LOJA ===")
        print("[1] Cadastrar cliente")
        print("[2] Listar clientes")
        print("[3] Deletar cliente")
        print("[4] Buscar cliente")
        print("[5] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            deletar_cliente()
        elif opcao == "4":
            buscar_cliente()
        elif opcao == "5":
            print("👋 Saindo do sistema...")
            break
       
        else:
            print("❌ Opção inválida!")

# BUSCAR CLIENTE POR NOME

def buscar_cliente():
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Digite o nome para buscar: ")

    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()

    if resultados:
        print("\n=== RESULTADOS ===")
        for c in resultados:
            print(f"""
ID: {c[0]}
Nome: {c[1]}
Telefone: {c[2]}
Idade: {c[3]}
Endereço: {c[4]}
Valor da compra: R${c[5]}
Data da compra: {c[6]}
-----------------------------""")
    else:
        print("❌ Nenhum cliente encontrado.")

    conn.close()


# =========================
# EXECUTAR SISTEMA
# =========================
if __name__ == "__main__":
    menu()