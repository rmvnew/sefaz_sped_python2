from image_recognition import find_image_on_screen
from mouse_control import click_on_location
from screen_capture import get_screenshot

import time

def execute_click_sequence():
    paths = [
        r'C:\PROJECTS\sped\img\click1.PNG',
        r'C:\PROJECTS\sped\img\click2.PNG',
        r'C:\PROJECTS\sped\img\click3.PNG',
        r'C:\PROJECTS\sped\img\click4.PNG',
        r'C:\PROJECTS\sped\img\click5.PNG',
        r'C:\PROJECTS\sped\img\click6.PNG',
    ]
    
    for index, path in enumerate(paths, start=1):  # Começa a contagem em 1
        try:
            
            print(f"Procurando pela imagem do clique {index}...\n")
            print("--------------------------------------\n")
            location = find_image_on_screen(path)
            if location:
                print(f"Clique {index} efetuado em: {location}")
                click_on_location(location)
                time.sleep(1)  # Espera 1 segundo antes do próximo clique
            else:
                print(f"Imagem {index} não encontrada: {path}")
        except Exception as e:
            print(f"Erro ao processar o clique {index} para {path}: {e}")

    print("Sequência de cliques finalizada.")





def buscar_arquivo_excel():
    print("A função para buscar o arquivo Excel ainda não foi implementada.")


def buscar_cadastrar_produtos():
    print("Buscando produtos...")
    # Função para buscar produtos.
    # Se não encontrar, chama a função para cadastrar produtos.
    print("Cadastrando produto...")
    # Função para cadastrar produtos.
