print('Bem-vindo a lista de contato de Geovana Soares')

contatos = {}
id_global = 5334697

#cadastro de contatos
def cadastrar_contato():
    global id_global

    print("----------------------------------------------")
    print("------------- MENU CADASTRAR CONTATO ---------")
    print("----------------------------------------------")
    print(f"Id do Contato: {id_global}")

    nome = str(input("Por favor entre com o nome do Contato: ").lower().strip())
    atividade = str(input("Por favor entre com a Atividade do contato: ").lower().strip())
    telefone = (input("Por favor entre com o telefone do contato: "))

    contatos[id_global] = {
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    print("\nContato cadastrado com sucesso!")
    id_global += 1

#consultar contatos
def consultar_contatos():
    print("----------------------------------------------")
    print("------------- MENU CONSULTAR CONTATOS --------")
    print("----------------------------------------------")
    print("1 - Consultar Todos os Contatos")
    print("2 - Consultar Contato por ID")
    print("3 - Consultar Contato(s) por Atividade")
    print("4 - Retornar")

    sub = input(">> ")

   #consultar todos contatos
    if sub == "1":
        if not contatos:
            print("Nenhum contato cadastrado.")
            return
        for cid, dados in contatos.items():
            print()
            print(f"id: {cid}")
            print(f"nome: {dados['nome']}")
            print(f"atividade: {dados['atividade']}")
            print(f"telefone: {dados['telefone']}")

    #consultar por id
    elif sub == "2":
        cid = int(input("Digite o id do contato: "))
        if cid in contatos:
            dados = contatos[cid]
            print(f"\nid: {cid}")
            print(f"nome: {dados['nome']}")
            print(f"atividade: {dados['atividade']}")
            print(f"telefone: {dados['telefone']}")
        else:
            print("Contato não encontrado.")

    #consultar por atividade
    elif sub == "3":
        atv = input("Digite a Atividade do(s) Contato(s): ")
        print()
        achou = False

        for cid, dados in contatos.items():
            if dados["atividade"].lower() == atv.lower():
                achou = True
                print(f"id: {cid}")
                print(f"nome: {dados['nome']}")
                print(f"atividade: {dados['atividade']}")
                print(f"telefone: {dados['telefone']}\n")

        if not achou:
            print("Nenhum contato encontrado com essa atividade.")

    elif sub == "4":
        return

    else:
        print("Opção inválida.")


#remover contato

def remover_contato():
    cid = int(input("Digite o id do contato a remover: "))
    if cid in contatos:
        del contatos[cid]
        print("Contato removido com sucesso.")
    else:
        print("Contato não encontrado.")


#menu principal
while True:
    print("\n------------------ MENU PRINCIPAL ------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")
    opcao = input(">> ").strip().lower()

    if opcao == "1":
        cadastrar_contato()

    elif opcao == "2" :
        consultar_contatos()

    elif opcao == "3":
        remover_contato()

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida! Tente novamente.")
