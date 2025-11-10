import os
from utils.arquivos import ler_dados, salvar_dados, ARQUIVO_USUARIOS

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def autenticarUsuario():
    print("|   AUTENTICAÇÃO DE USUÁRIO   |")
    login = input("|Login: ")
    senha = input("|Senha: ")
    
    usuarios = ler_dados(ARQUIVO_USUARIOS)
    
    for u in usuarios:
        if u['login'] == login and u['senha'] == senha:
            print(f"\n[SUCESSO] Login realizado. Bem-vindo(a), {u['nome']}!")
            return u['login'] # Retorna o login para ser usado no main
            
    print("\n[ERRO] Login ou senha inválidos.")
    return None

def cadastrarUsuario():
    print("|    CADASTRO DE NOVO USUÁRIO   |")
    nome = input("|Nome completo: ")
    email = input("|Email: ")
    login = input("|Login (username): ")
    
    usuarios = ler_dados(ARQUIVO_USUARIOS)
    
    # Verifica se o login já existe
    for u in usuarios:
        if u['login'] == login:
            input(f"\n[ERRO] O login '{login}' já existe. Tente outro. Pressione Enter para continuar...")
            limparTela()
            return

    senha = input("Senha: ")
    
    novoUsuario = {
        'nome': nome,
        'email': email,
        'login': login,
        'senha': senha
    }
    
    usuarios.append(novoUsuario)
    salvar_dados(ARQUIVO_USUARIOS, usuarios)
    input(f"\n[SUCESSO] Usuário '{login}' cadastrado com sucesso! Pressione Enter para continuar...")
    limparTela()
