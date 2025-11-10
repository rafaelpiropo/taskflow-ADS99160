import usuarios, tarefas, relatorioProdutividade, os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
    usuarioLogado = None
    print("Bem-vindo ao sistema de gerenciamento de tarefas.")
    while True:
        if usuarioLogado is None:
            print('_=+=+=+=+=+=+=+=+=+=+=+_')
            print('|    MENU PRINCIPAL    |')
            print('*----------------------*')
            print('|[1] Realizar Login    |')
            print('|[2] Cadastrar Usuário |')
            print('|[3] Sair              |')
            print('*----------------------*')
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha == 1:
                    pass
                    # usuarioLogado = usuarios.autenticarUsuario()
                    limparTela()
                elif escolha == 2:
                    pass
                    # usuarios.cadastrarUsuario()
                    limparTela()
                elif escolha == 3:
                    pass
                    print("Saindo do sistema.")
                    break
                else:
                    input("Opção inválida. Tente novamente. Pressione Enter para continuar...")
                    limparTela()
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                continue

        else:
            print(f'LOGADO COMO: {usuarioLogado}')
            print('_=+=+=+=+=+=+=+=+=+=+=+=+=_')
            print('|[1] Gerenciar Tarefas    |')
            print('|[2] Ver Relatórios       |')
            print('|[3] Fazer Logout         |')
            print('*-------------------------*')
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha == 1:
                    menuTarefas()
                    limparTela()
                    pass
                elif escolha == 2:
                    limparTela()
                    pass
                elif escolha == 3:
                    usuarioLogado = None
                    input("Logout realizado com sucesso. Pressione Enter para continuar...")
                    limparTela()
                else:
                    input("Opção inválida. Tente novamente. Pressione Enter para continuar...")
                    limparTela()
            except ValueError:
                input("Entrada inválida. Por favor, insira um número. Pressione Enter para continuar...")
                limparTela()
                continue

def menuTarefas(loginUsuario):
    while True:
        print(f"MENU DE TAREFAS (Usuário: {loginUsuario})")
        print("_=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_")
        print("|[1] Cadastrar Tarefa         |")
        print("|[2] Listar Minhas Tarefas    |")
        print("|[3] Editar Tarefa            |")
        print("|[4] Concluir Tarefa          |")
        print("|[5] Excluir Tarefa           |")
        print("|[6] Voltar ao Menu Principal |")
        print("*-----------------------------*")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                pass
                # tarefas.cadastrarTarefa(loginUsuario)
            elif opcao == 2:
                pass
                # tarefas.listarTarefas(loginUsuario)
            elif opcao == 3:
                pass
                # tarefas.editarTarefa(loginUsuario)
            elif opcao == 4:
                pass
                # tarefas.concluirTarefa(loginUsuario)
            elif opcao == 5:
                pass
                # tarefas.excluirTarefa(loginUsuario)
            elif opcao == 6:
                limparTela()
                break
            else:
                input("Opção inválida. Tente novamente. Pressione Enter para continuar...")
        except Exception as e:
            input(f"Erro: {e}. Pressione Enter para continuar...")
            continue
