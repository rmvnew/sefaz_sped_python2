from actions import (execute_click_sequence,buscar_arquivo_excel,read_data)

def menu():
    while True:
        print("1 - Buscar arquivo Excel")
        print("2 - Iniciar bateria de cliques")
        print("3 - Buscar e cadastrar produtos")
        print("4 - Buscar arquivo Excel")
        print("5 - Ler lista")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Implementar a lógica para buscar o arquivo Excel
            pass
        elif opcao == '2':
            execute_click_sequence()
        elif opcao == '3':
            # Implementar a lógica de busca e cadastro de produtos
            pass
        elif opcao == '4':
            buscar_arquivo_excel()
        elif opcao == '5':
            read_data()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
