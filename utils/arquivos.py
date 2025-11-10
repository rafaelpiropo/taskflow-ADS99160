import json, os

# Aqui é definido os arquivos que serão utilizados para armazenar os dados
ARQUIVO_USUARIOS = 'usuarios.txt'
ARQUIVO_TAREFAS = 'tarefas.txt'

def ler_dados(arquivo):
    """
    Lê dados de um arquivo .txt (Mas ta no formato JSON, estruturado no caso).
    Retorna uma lista vazia se o arquivo não existir ou estiver vazio.
    """
    # Verifica se o arquivo existe
    if not os.path.exists(arquivo):
        return [] # Retorna lista vazia se o arquivo não existir
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return dados     
    except Exception as e:
        print(f"Erro ao ler dados de {arquivo}: {e}")
        return [] # Retorna lista vazia se apresentar qualquer tipo de erro

def salvar_dados(arquivo, dados):
    """
    Salva dados em um arquivo .txt (Mas de novo, colocamos em formato JSON).
    """
    try:
        with open(arquivo, 'w', encoding='utf-8') as arq:  
            json.dump(dados, arq, indent=4, ensure_ascii=False) 
            # Aqui o dump ta só salvando os dados no arquivo txt em formato JSON com identação de 4 espaços
            # E o ensure_ascii=False é pra garantir que caracteres especiais sejam salvos corretamente
    except Exception as e:
        print(f"Erro ao salvar dados em {arquivo}: {e}") # Retorna essa mensagem se apresentar qualquer tipo de erro
