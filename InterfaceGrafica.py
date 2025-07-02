from Usuario import Usuario
from UsuarioDOA import UsuarioDAO
class InterfaceGrafica:
    def menu_principal(self):
        while True:
            print("""
⢋⣴⠒⡝⣿⣿⣿⣿⣿⡿⢋⣥⣶⣿⣿⣿⣿⣿⣿⣶⣦⣍⠻⣿⣿⣿⣿⣿⣷⣿
⢾⣿⣀⣿⡘⢿⣿⡿⠋⠄⠻⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣿⣿
⠄⠄⠈⠙⢿⣦⣉⡁⠄⠄⣴⣶⣿⣿⢷⡶⣾⣿⣿⣿⣿⡛⠛⠻⠃⠙⢿⣿⣿⣿
⠄⠄⠄⠄⠄⠈⠉⣀⣀⣴⡟⢩⠁⠩⣝⢂⢨⣿⣿⣿⣿⢟⡛⣳⣶⣤⡘⠿⢋⣡
⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣾⣿⣶⣿⣿⣿⣿⣿⣿⣿⣆⣈⣱⣮⣿⣷⡾⠟⠋
⠄⠄⠄⠄⠄⠄⠄⠈⠿⠛⠛⣻⣿⠉⠛⠋⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠸⣿
⠄⠄⠄⠄⢀⡠⠄⢒⣤⣟⠿⣿⣿⣿⣷⣤⣤⣀⣀⣉⣉⣠⣽⣿⣟⠻⣿⣿⡆⢻
⠄⣀⠄⠄⠄⠄⠈⠋⠉⣿⣿⣶⣿⣟⣛⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⡇⣸
⣿⠃⠄⠄⠄⠄⠄⠄⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⠁⢿
⡋⠄⠄⠄⠄⠄⠄⢰⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
            """)
            print("========================")
            print("JOGOS DB - Menu Principal")
            print("========================")
            print("1 - Cadastrar Jogo")
            print("2 - Cadastrar Usuário")
            print("3 - Registrar Aquisição")
            print("4 - Listar Jogos")
            print("5 - Listar Usuários")
            print("6 - Buscar Jogo por Nome")
            print("7 - Buscar Jogo por Categoria")
            print("8 - Buscar Jogo por Editora")
            print("9 - Atualizar Jogo")
            print("10 - Atualizar Usuário")
            print("11 - Deletar Jogo")
            print("12 - Deletar Usuário")
            print("0 - Sair")
            print("========================")

            try:
                opcao = int(input("Digite uma opção [0-12]: "))
            except ValueError:
                print("Opção inválida! Digite um número.")
                continue

            if opcao == 1:
                self.adicionar_jogo()
            elif opcao == 2:
                self.adicionar_usuario()
            elif opcao == 3:
                self.registrar_aquisicao()
            elif opcao == 4:
                self.listar_jogos()
            elif opcao == 5:
                self.listar_usuarios()
            elif opcao == 6:
                self.buscar_jogo_por_nome()
            elif opcao == 7:
                self.buscar_jogo_por_categoria()
            elif opcao == 8:
                self.buscar_jogo_por_editora()
            elif opcao == 9:
                self.atualizar_jogo()
            elif opcao == 10:
                self.atualizar_usuario()
            elif opcao == 11:
                self.deletar_jogo()
            elif opcao == 12:
                self.deletar_usuario()
            elif opcao == 0:
                print("Saindo do sistema. Até a próxima, aventureiro!")
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    def menuListarTodosUsuarios(self):
        dao = UsuarioDAO()
        print ('Listando Usuários...')
        pessoas = dao.listarUsuarios()
        encontrou = False
        for p in pessoas:
            encontrou = True
            print("Id = {} - Nome = {} - Login = {}".format(p.id, p.nome,p.login))
        if not encontrou:
            print ('Nenhum Registro Encontrado')
        self.menu_principal
    
    def menuInserirUser(self):
        dao = UsuarioDAO()
        nome = input ("Nome do Usuário:")
        email = input ("Email do Usuário:")
        senha = input ("Senha do Usuário:")
        sucess = dao.inserirUsuario(nome, email, senha)
        if sucess:
            print ("Usuario Inserido Com Sucesso!")
        else:
            print ("Erro ao Inserir o Usuário")
        self.menu_principal()


if __name__ == '__main__':
    gui = InterfaceGrafica()
    gui.menu_principal()


