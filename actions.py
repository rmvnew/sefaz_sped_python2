from image_recognition import find_image_on_screen
from mouse_control import click_on_location
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from products import Product

import time


product_list = []

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
    
    root = tk.Tk()
    root.withdraw()  # Fecha a janela principal

    # Abre a janela de seleção de arquivo
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])

    # Verifica se um arquivo foi selecionado
    if file_path:
        # Carrega o arquivo Excel em um DataFrame pandas
        excel_data = pd.read_excel(file_path,skiprows=1)

        select_colunms = excel_data[['CÓDIGO','DESCRIÇÃO','QUANTIDADE']] 

        

        for index,row in select_colunms.iterrows():
            product = Product(index,row['CÓDIGO'],row['DESCRIÇÃO'],row['QUANTIDADE'])
            product_list.append(product)

        
def read_data():

     for product in product_list:
            print(product)       


def buscar_cadastrar_produtos():
    print("Buscando produtos...")
    # Função para buscar produtos.
    # Se não encontrar, chama a função para cadastrar produtos.
    print("Cadastrando produto...")
    # Função para cadastrar produtos.
