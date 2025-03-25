import sqlite3
from sqlite3 import Error

def criar_conexao():
    try:
        # Cria ou conecta ao banco de dados
        conexao = sqlite3.connect('usuarios.db')
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()
        
        # Cria a tabela de usuários
        sql_criar_tabela = '''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''
        
        cursor.execute(sql_criar_tabela)
        conexao.commit()
        print("Tabela criada com sucesso!")
        
    except Error as e:
        print(f"Erro ao criar tabela: {e}")

def inserir_usuario(conexao, nome, email, senha):
    try:
        cursor = conexao.cursor()
        
        sql_inserir = '''INSERT INTO usuarios (nome, email, senha)
                        VALUES (?, ?, ?)'''
                        
        cursor.execute(sql_inserir, (nome, email, senha))
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
        
    except Error as e:
        print(f"Erro ao inserir usuário: {e}")

def buscar_usuario_por_email(conexao, email):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        return cursor.fetchone()
    except Error as e:
        print(f"Erro ao buscar usuário: {e}")
        return None

def atualizar_usuario(conexao, id, nome, email):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE usuarios 
            SET nome = ?, email = ?
            WHERE id = ?""", (nome, email, id))
        conexao.commit()
        print("Usuário atualizado com sucesso!")
    except Error as e:
        print(f"Erro ao atualizar usuário: {e}")

def deletar_usuario(conexao, id):
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conexao.commit()
        print("Usuário deletado com sucesso!")
    except Error as e:
        print(f"Erro ao deletar usuário: {e}")

# Exemplo de uso
if __name__ == "__main__":
    # Criar conexão com o banco
    conexao = criar_conexao()
    
    if conexao is not None:
        # Criar tabela
        criar_tabela(conexao)
        
        # Exemplo de inserção de usuário
        inserir_usuario(conexao, "João Silva", "joao@email.com", "senha123")
        
        # Fechar conexão
        conexao.close()